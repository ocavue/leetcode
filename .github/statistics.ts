import jsyaml from 'js-yaml'
import * as fs from 'fs'
import path from 'path'
import _ from 'lodash'

type Lang = "py" | 'go'

interface Header {
    submits: {
        date: string,
        cheating: boolean,
        minutes: number,
    }[]
    labels?: string[],
    comment?: string,
}

interface Question {
    id: number,
    lang: Lang,
    header: Header,
}

function parse_header(lang: Lang, file_lines: string[]): Header {

    let header_from, header_end: string

    if (lang == "py") {
        header_from = '"""'
        header_end = '"""'
    } else {
        header_from = "/*"
        header_end = "*/"
    }

    let from_line_index = file_lines.indexOf(header_from)
    let to_line_index = file_lines.indexOf(header_end, from_line_index + 1)
    let header_lines = file_lines.slice(from_line_index + 1, to_line_index)
    let header_text = header_lines.join('\n')
    let raw = jsyaml.load(header_text)
    let header: Record<string, any> = {}

    for (let field of ['submits', 'labels', 'comment'] as const) {
        header[field] = raw[field]
        delete raw[field]
    }
    if (raw.length >= 1) {
        throw Error("unknow field: " + JSON.stringify(raw))
    }

    return header as Header
}


function walk_questions() {
    let root = path.join(
        path.resolve("."),
    )

    let files = fs.readdirSync(
        root,
        {
            encoding: 'utf-8'
        }
    )

    let questions: Question[] = []

    for (let file of files) {
        let matched = /^([0-9]+)\..+\.(py|go)$/.exec(file)
        if (matched) {
            try {
                let id = Number(matched[1])
                let lang = matched[2] as Lang
                let text = fs.readFileSync(file, { encoding: 'utf-8' })
                let lines = text.split('\n')
                questions.push(
                    {
                        id,
                        lang,
                        header: parse_header(lang, lines),
                    }
                )
            } catch (error) {
                console.error('failed to parsing', file)
                throw error
            }
        }
    }

    return questions
}

function getSorkKey(question: Question): number {
    let submits = question.header.submits
    let lastSubmit = submits[submits.length - 1]

    // 没做出来的排在前面
    // 提交比较早的排在前面
    return (
        lastSubmit.cheating ? 0 : Date.parse('2099-01-01T01:01:01') +
        Date.parse(lastSubmit.date)
    )
}


function sort_questions(questions: Question[]) {
    return _.sortBy(
        questions,
        getSorkKey
    )
}

function main() {
    console.log(
        JSON.stringify(
            sort_questions(walk_questions()),
            null,
            "  ",
        )
    )
}

main()