import jsyaml from 'js-yaml'
import * as fs from 'fs'
import path from 'path'
import _ from 'lodash'
import Ajv from 'ajv'

type Lang = "py" | 'go'

interface Header {
    submits: {
        date: Date,
        cheating: boolean,
        minutes: number,
    }[]
    labels?: string[],
    comment?: string,
}

interface Question {
    id: number,
    lang: Lang,
    file: string,
    header: Header,
}

function validate_header(header: Header) {
    let ajv = new Ajv()
    let validate = ajv.compile({
        type: "object",
        required: ["submits"],
        properties: {
            "submits": {
                type: "array",
                items: {
                    type: "object",
                    required: ["date", "cheating"],
                    properties: {
                        "date": { type: "object" },
                        "cheating": { type: "boolean" },
                        "minutes": { type: "integer", default: 60 },
                    }
                },
                minItems: 1,
            },
            "labels": {
                type: "array",
                items: {
                    type: "string"
                }
            },
            "comment": {
                type: "string",
            }
        }
    });
    let valid = validate(header);
    if (!valid) throw validate.errors
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

    validate_header(raw)
    return raw as Header
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
                        file,
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
    let key = lastSubmit.cheating ? 0 : Date.parse('2099-01-01T01:01:01')
    key += lastSubmit.date.getTime()
    return key
}


function sort_questions(questions: Question[]) {
    return _.sortBy(
        questions,
        getSorkKey
    )
}

function print(obj: any) {
    console.log(
        JSON.stringify(
            obj,
            null,
            "  ",
        )
    )
}

function main() {
    const questions = sort_questions(walk_questions())
    if (process.env.LEETCODE_NEXT) {
        let question = questions[0]
        let submits = question.header.submits
        let lastSubmit = submits[submits.length - 1]

        console.log({
            file: question.file,
            cheating: lastSubmit.cheating,
            date: lastSubmit.date,
            minutes: lastSubmit.minutes,
        })
    }
    else {
        print(questions)
    }
}

main()