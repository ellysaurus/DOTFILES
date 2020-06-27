import { Range } from 'vscode-languageserver'

export interface Settings {
  highlightEnable: boolean
  colorsEnable: boolean
  disableLanguages: string[]
}

export interface DocumentSymbol {
  text: string
  range: Range
}

