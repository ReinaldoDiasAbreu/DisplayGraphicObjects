import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width:  800 //1366
    height: 800 //768
    title: qsTr('Display Graphic Objects')
    font.pixelSize: 15
    Material.theme: 'Dark'

    menuBar: MenuBar {
        Menu {
            id: menu
            title: qsTr("File")
            MenuItem{
                id: file
                text: 'Open'
                onClicked: {
                    bridge.open_file()
                }
            }
        }
    }

    Row{
        id: row_1
        spacing: 20
        anchors{
            horizontalCenter: parent.horizontalCenter
            topMargin: 20
        }
    }
    
}