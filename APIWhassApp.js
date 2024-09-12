//funcion que llama a createMenus
function onOpen() {
    createMenus();
}

// la funcion createMenus crea un menu en la hoja sheet y se agregan items 
function createMenus() {
    var menu = SpreadsheetApp.getUi().createMenu("Whatsapp") // llama a la hoja de calculo y se crea un menu con titulo de whatsapp
    menu.addItem('Notificar Whatsapp', 'enviarwhatsapp'); //se colocan 2 items
    menu.addToUi(); // metodo que permite visualizar el  menú y sus elementos sean visibles y accesibles para los usuarios de la hoja de cálculo.
}

// funcion muestra un cuadro con botones "Sí" y "No", y guarda la respuesta del usuario
function enviarwhatsapp() {
    var response = "No"
    try { 
        var response = Browser.msgBox('Seguro que quiere enviar msj ahora ?', Browser.Buttons.YES_NO);
    } catch (e) {
        Browser.msgBox('La acción no se ha realizado', Browser.Buttons.OK);
    }
    if (response == "yes") { // verificar si la respuesta del usuario fue si 
        enviar();
        console.log("Funcion fin programar : la fecha y hora: " + new Date()); //  Registra la fecha y hora actuales en la consola
        Browser.msgBox('La acción ha sido realizada', Browser.Buttons.OK); //Muestra un mensaje confirmando que la acción se ha realizado
    }
}


function enviar() {
    var excel = SpreadsheetApp.getActiveSpreadsheet();
    var sheet_configuracion = excel.getSheetByName("Configuracion");// nombre de la hoja de calculo que extrae la informacion 
    var plantilla = sheet_configuracion.getRange(2, 2).getValue();// primero es la fila las segunda es la columna 
    var token = sheet_configuracion.getRange(2, 3).getValue();
    var api = sheet_configuracion.getRange(2, 4).getValue();

  if (excel.getSheetByName("Envio-mensaje")) {
        var sheet = excel.getSheetByName("Envio-mensaje");// si existe la hoja envio mensaje guardelo en la variable sheet
        var rows = sheet.getRange(3, 2, sheet.getLastRow() - 1, sheet.getLastColumn()).getValues(); //posicion de los valores a tomar en la hoja de configuracion el getValues devuelve el rango como una matriz bidimencional 
        for (var i = 0, l = rows.length; i < l; i++) {//
            var telefono = rows[i][0];
            var mensaje = rows[i][1];
            //contruccion del Payload
            var payload = { 
                "messaging_product": "whatsapp",
                "to": telefono,
                "type": "template",
                "template": {
                    "name": plantilla,
                    "language":{
                        "code": "en_US"
                    },
                "components": [{
                  "type": "body",
                  "parameters": [{
                            "type": "text",
                            "text": mensaje
                                }]
                }]
                }
            }
            var options =
            {
              'headers': { "Content-Type": "application/json","Authorization": token},
                'method': "POST",
                'payload': JSON.stringify(payload)
            };
            try {
                var response = UrlFetchApp.fetch(api, options);
                var json = JSON.parse(response.getContentText());
            } catch (e) {
            }
        }
    }
}

