import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    title: qsTr("Hello World")
    width: 640
    height: 480
    visible: true
    color: "white"

    ColumnLayout {
        anchors.fill: parent

        Rectangle {
            id: bigBox
            height: root.height - 200
            width: root.width

            Rectangle {
                anchors.centerIn: parent
                width: 400
                height: 200
                radius: 10
                color: "#b9d795"

                // Because we need select the text
                TextEdit {
                    id: wordTxt
                    anchors.centerIn: parent
                    readOnly: true
                    height: 200
                    width: 400
                    font.pixelSize: 40
                    text: "Click Next"
                    selectByMouse: true
                }
            }
        }

        Text {
            id: numbersTxt
            text: wordslist.len()
        }

        TextField {
            id: answerTxt

            background: Rectangle {
                implicitWidth: root.width - 10
                implicitHeight: 40
                color: "transparent"
                border.color: "#21be2b"
            }
        }

        RowLayout {
            anchors.bottom: root.bottom

            LButton {
                id: nextBttn
                text: "Next"
                onClicked: {
                    answerTxt.text = ""
                    playBttn.enabled = true
                    wordslist.next()
                    wordTxt.text = "?"
                    numbersTxt.text = wordslist.len()
                    wordslist.play()
                }
            }

            LButton {
                id: playBttn
                text: "Play"
                onClicked: {
                    playBttn.enabled = false
                    wordslist.play()
                    playBttn.enabled = true
                }
            }

            LButton {
                id: showBttn
                text: "Show"
                onClicked: {
                    var word = wordslist.show()
                    wordTxt.text = word
                }
            }
        }
    }
}
