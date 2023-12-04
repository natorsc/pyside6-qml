import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: app

    height: Screen.height / 2
    minimumHeight: Screen.height / 3
    minimumWidth: Screen.height / 3
    title: qsTr('Python e Qt 6: PySide6 QML Button')
    visible: true
    width: Screen.width / 2
    x: 40
    y: 50

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 12
        spacing: 6

        Button {
            Layout.alignment: Qt.AlignCenter
            text: qsTr('Clique aqui')

            onClicked: {
                console.log(qsTr('Botão pressionado.'));
                mainwindow.on_button_clicked();
            }
        }
    }
}
