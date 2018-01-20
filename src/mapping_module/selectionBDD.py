import sqlite3

def getProperties(conn,emotion):

        c = conn.cursor()

        c.execute('''SELECT P.leds_color, P.leds_frequence, P.leds_intensite, P.leds_texte, P.secondary_color, P.list_color
                  from Emotions E, Properties P
                  where E.propertyID = P.id 
                  AND E.nom = ?
                  ''',[emotion])


        result=c.fetchall()
        return result

def getAnimation(conn,emotion):

        c = conn.cursor()

        c.execute('''SELECT A.id , A.nom, A.lien, A.frequence, A.intensite
                  from Emotions E, Animations A
                  where E.animationID = A.id 
                  AND E.nom = ?
                  ''',[emotion])


        result=c.fetchall()
        return result

