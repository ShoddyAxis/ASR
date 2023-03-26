import fitz
from fitz.utils import getColor


def repagn(idn, so, nd, infc, ub, ni, dif, stif):
    ids = idn
    infs = ni
    # Nuevo documento
    doc = fitz.open()
    # Nueva página en el documento. Se insertará tras la última página
    pagina = doc.new_page(pno=-1, width=2000, height=2000)
    pagina.insert_font(fontname="Luois", fontfile="fuentes/Louis George Cafe.ttf")
    # Establecemos la posición sobre la que vamos a dibujar
    c1 = getColor("red")
    c2 = getColor("aliceblue")
    c3 = getColor("black")
    pagina.draw_line(p1=fitz.Point(100, 100), p2=fitz.Point(1900, 100), color=c1, width=5, overlay=True)
    pagina.draw_line(p1=fitz.Point(100, 100), p2=fitz.Point(100, 1900), color=c1, width=5, overlay=True)
    pagina.draw_line(p1=fitz.Point(100, 1900), p2=fitz.Point(1900, 1900), color=c1, width=5, overlay=True)
    pagina.draw_line(p1=fitz.Point(1900, 100), p2=fitz.Point(1900, 1900), color=c1, width=5, overlay=True)
    # Insertamos un texto en la página
    if so.__eq__('Ubuntu'):
        x1c1 = 600
        y1c1 = 1000
        x2c1 = 1000
        y2c1 = 1120
        x1c2 = 1000
        x2c2 = 1400
        x1t1 = 620
        x2t1 = 980
        x1t2 = 1020
        x2t2 = 1380
        y1t1 = 1020
        y2t1 = 1090
        pagina.insert_textbox((150, 200, 2330, 600), fontsize=70, align=fitz.TEXT_ALIGN_JUSTIFY, fontname="Luois",
                              buffer="Administracion de Servicios en Red\nPractica 1\nBlancas Martinez Mariana Jocelyn"
                                     "4CM14\n")
        pagina.insert_textbox((200, 500, 2330, 1200), fontsize=70, align=fitz.TEXT_ALIGN_JUSTIFY, fontname="Luois",
                              buffer="Informacion del Agente")
        posicion = fitz.Point(300, 650)
        pagina.insert_text(posicion, "Sistema Operativo: ", fontsize=60)
        posicion = fitz.Point(820, 650)
        pagina.insert_text(posicion, so, fontsize=60)
        pagina.insert_image(rect=(1400, 350, 1800, 750), filename="imagenes/Ubuntu_logo.png", keep_proportion=False,
                            overlay=True)
        posicion = fitz.Point(300, 750)
        pagina.insert_text(posicion, "Nombre del Dispositivo: ", fontsize=60)
        posicion = fitz.Point(950, 750)
        pagina.insert_text(posicion, nd, fontsize=60)
        posicion = fitz.Point(300, 850)
        pagina.insert_text(posicion, "Informacion de contacto: ", fontsize=60)
        posicion = fitz.Point(970, 850)
        pagina.insert_text(posicion, infc, fontsize=60)
        posicion = fitz.Point(300, 950)
        pagina.insert_text(posicion, "Ubicacion: ", fontsize=60)
        posicion = fitz.Point(600, 950)
        pagina.insert_text(posicion, ub, fontsize=60)
        rect = fitz.Rect(600, 1000, 1000, 1120)
        pagina.insert_textbox((620, 1020, 980, 1090), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                              overlay=True,
                              buffer="Interfaz")
        pagina.draw_rect(rect, color=c3, fill=c2, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=False,
                         morph=None,
                         stroke_opacity=1, fill_opacity=3, oc=0)
        rect = fitz.Rect(1000, 1000, 1400, 1120)
        pagina.insert_textbox((1020, 1020, 1380, 1090), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                              overlay=True,
                              buffer="Estado")
        pagina.draw_rect(rect, color=c3, fill=c2, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=False,
                         morph=None,
                         stroke_opacity=1, fill_opacity=1, oc=0)
        if infs >= 5:
            infs = 5
        for n in range(infs):
            y1c1 += 120
            y2c1 += 120
            y1t1 += 120
            y2t1 += 120
            rect = fitz.Rect(x1c1, y1c1, x2c1, y2c1)
            pagina.insert_textbox((x1t1, y1t1, x2t1, y2t1), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                                  overlay=True,
                                  buffer=dif[n - 1])
            pagina.draw_rect(rect, color=None, fill=None, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=True,
                             morph=None,
                             stroke_opacity=1, fill_opacity=1, oc=0)
            rect = fitz.Rect(x1c2, y1c1, x2c2, y2c1)
            pagina.insert_textbox((x1t2, y1t1, x2t2, y2t1), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                                  overlay=True,
                                  buffer=stif[n - 1])
            pagina.draw_rect(rect, color=None, fill=None, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=True,
                             morph=None,
                             stroke_opacity=1, fill_opacity=1, oc=0)
    if so.__eq__('Windows'):
        x1c1 = 300
        y1c1 = 1000
        x2c1 = 1100
        y2c1 = 1120
        x1c2 = 1100
        x2c2 = 1500
        x1t1 = 320
        x2t1 = 1120
        x1t2 = 1120
        x2t2 = 1480
        y1t1 = 1020
        y2t1 = 1090
        pagina.insert_textbox((150, 200, 2330, 600), fontsize=70, align=fitz.TEXT_ALIGN_JUSTIFY, fontname="Luois",
                              buffer="Administracion de Servicios en Red\nPractica 1\nBlancas Martinez Mariana Jocelyn"
                                     " 4CM14\n")
        pagina.insert_textbox((200, 500, 2330, 1200), fontsize=70, align=fitz.TEXT_ALIGN_JUSTIFY, fontname="Luois",
                              buffer="Informacion del Agente")
        posicion = fitz.Point(300, 650)
        pagina.insert_text(posicion, "Sistema Operativo: ", fontsize=60)
        posicion = fitz.Point(820, 650)
        pagina.insert_text(posicion, so, fontsize=60)
        pagina.insert_image(rect=(1400, 350, 1800, 750), filename="imagenes/Windows-Logo.png",
                            keep_proportion=False,
                            overlay=True)
        posicion = fitz.Point(300, 750)
        pagina.insert_text(posicion, "Nombre del Dispositivo: ", fontsize=60)
        posicion = fitz.Point(950, 750)
        pagina.insert_text(posicion, nd, fontsize=60)
        posicion = fitz.Point(300, 850)
        pagina.insert_text(posicion, "Informacion de contacto: ", fontsize=60)
        posicion = fitz.Point(970, 850)
        pagina.insert_text(posicion, infc, fontsize=60)
        posicion = fitz.Point(300, 950)
        pagina.insert_text(posicion, "Ubicacion: ", fontsize=60)
        posicion = fitz.Point(600, 950)
        pagina.insert_text(posicion, ub, fontsize=60)
        rect = fitz.Rect(300, 1000, 1100, 1120)
        pagina.insert_textbox((320, 1020, 1080, 1090), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                              overlay=True,
                              buffer="Interfaz")
        pagina.draw_rect(rect, color=c3, fill=c2, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=False,
                         morph=None,
                         stroke_opacity=1, fill_opacity=3, oc=0)
        rect = fitz.Rect(1100, 1000, 1500, 1120)
        pagina.insert_textbox((1120, 1020, 1480, 1090), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                              overlay=True,
                              buffer="Estado")
        pagina.draw_rect(rect, color=c3, fill=c2, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=False,
                         morph=None,
                         stroke_opacity=1, fill_opacity=1, oc=0)
        if infs >= 5:
            infs = 6
        for n in range(1,infs):
            y1c1 += 120
            y2c1 += 120
            y1t1 += 120
            y2t1 += 120
            rect = fitz.Rect(x1c1, y1c1, x2c1, y2c1)
            pagina.insert_textbox((x1t1, y1t1, x2t1, y2t1), fontsize=50, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                                  overlay=True,
                                  buffer=dif[n - 1])
            pagina.draw_rect(rect, color=None, fill=None, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=True,
                             morph=None,
                             stroke_opacity=1, fill_opacity=1, oc=0)
            rect = fitz.Rect(x1c2, y1c1, x2c2, y2c1)
            pagina.insert_textbox((x1t2, y1t1, x2t2, y2t1), fontsize=60, align=fitz.TEXT_ALIGN_CENTER, fontname="Luois",
                                  overlay=True,
                                  buffer=stif[n - 1])
            pagina.draw_rect(rect, color=None, fill=None, width=2, dashes=None, lineCap=0, lineJoin=0, overlay=True,
                             morph=None,
                             stroke_opacity=1, fill_opacity=1, oc=0)
    """pagina.insert_text(posicion, "Nombre del Dispositivo: " , fontsize=80)
    posicion = fitz.Point(1260, 900)
    pagina.insert_text(posicion, "Linux" , fontsize=80)"""
    # Guardamos los cambios en el documento
    doc.write()
    # Guardamos el fichero PDF
    nom = 'ReporteAgente#' + str(ids) + '.pdf'
    doc.save(nom, pretty=True)
