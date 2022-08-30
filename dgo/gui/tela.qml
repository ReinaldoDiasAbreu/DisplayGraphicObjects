import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Dialogs
import QtQuick.Layouts
import QtQuick.Shapes


ApplicationWindow {
    visible: true
    width:  1366
    height: 768
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

            var objetos = bridge.get_objs()
            console.log( objetos )
            
        }
        onRejected: {
            console.log("Canceled Open File")
        }
    }
    
    GridLayout {
        id: grid
        rows: 12
        columns: 12
        anchors.fill: parent

        property double colMulti : grid.width / grid.columns
        property double rowMulti : grid.height / grid.rows
        function prefWidth(item){
            return colMulti * item.Layout.columnSpan
        }
        function prefHeight(item){
            return rowMulti * item.Layout.rowSpan
        }

        Rectangle {
            color : "transparent"
            Layout.rowSpan   : 10
            Layout.columnSpan: 2
            Layout.preferredWidth  : grid.prefWidth(this)
            Layout.preferredHeight : grid.prefHeight(this)
        }

        Rectangle {
            Layout.rowSpan   : 10
            Layout.columnSpan: 10
            Layout.preferredWidth  : grid.prefWidth(this)
            Layout.preferredHeight : grid.prefHeight(this)
                
                Shape {
                    width: 200
                    height: 150
                    anchors.centerIn: parent
                    ShapePath {
                        strokeWidth: 4
                        strokeColor: "red"
                        strokeStyle: ShapePath.DashLine
                        dashPattern: [ 1, 4 ]
                        startX: 20; startY: 20
                        PathLine { x: 20; y: 20 }
                    }

                }            
        }

        Rectangle {
            id : greenRect
            color : "transparent"
            Layout.rowSpan : 2
            Layout.columnSpan : 12
            Layout.preferredWidth  : grid.prefWidth(this)
            Layout.preferredHeight : grid.prefHeight(this)

        }

    }

    
}