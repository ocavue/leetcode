import jsyaml from 'js-yaml'
import * as fs from 'fs'
import path from 'path'

type Lang = "py" | 'go'

interface Header {
    submits?: {
        date: number,
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
    let header: Header = {}

    for (let field of ['submits', 'labels', 'comment'] as const) {
        header[field] = raw[field]
        delete raw[field]
    }
    if (raw.length >= 1) {
        throw Error("unknow field: " + JSON.stringify(raw))
    }

    return header
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
            console.log('parsing', file)

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
        }

    }

    return JSON.stringify(questions, null, "  ")
}

function main() {
    console.log(
        walk_questions()
    )
}

main()