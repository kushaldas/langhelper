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

    ColumnLayout {
        anchors.fill: parent

        Rectangle {
            id: bigBox
            height: root.height - 100
            width: root.width

            Rectangle {
                anchors.centerIn: parent
                width: 440
                height: 200
                radius: 10
                color: "#b9d795"

                Text {
                    id: wordTxt
                    anchors.centerIn: parent
                    height: 200
                    width: 400
                    font.pixelSize: 40
                    text: "Click Next"
                }
            }
        }

        RowLayout {
            anchors.bottom: root.bottom

            LButton {
                id: nextBttn
                text: "Next"
                onClicked: {

                    wordslist.next()
                    wordTxt.text = "?"
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
