import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Dialogs

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
                onTriggered: {
                    fileDialog.open()
                }
            }
        }
    }

    FileDialog {
        id: fileDialog
        title: "Please choose a file"
        nameFilters: [ "XML files (*.xml)"]
        onAccepted: {
            var file_url = fileDialog.selectedFile
            bridge.open_file(file_url)
        }
        onRejected: {
            console.log("Canceled Open File")
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