import sqlite3

conn = sqlite3.connect('WALL-E-Motion.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Properties
            (id INT PRIMARY KEY NOT NULL,leds_color VARCHAR(100),leds_frequence VARCHAR(100),leds_intensite VARCHAR(100),leds_texte VARCHAR(100),secondary_color VARCHAR(100),list_color VARCHAR(100))''')

c.execute('''CREATE TABLE Animations
            (id INT PRIMARY KEY NOT NULL,nom VARCHAR(100),lien VARCHAR(100),frequence VARCHAR(100),intensite VARCHAR(100))''')

c.execute('''CREATE TABLE Emotions
            (id INT PRIMARY KEY NOT NULL,nom VARCHAR(100),
            propertyID int,
            animationID int,
            FOREIGN KEY(propertyID) REFERENCES Properties(id),
            FOREIGN KEY (animationID) REFERENCES Animations(id))''')



# Save (commit) the changes
conn.commit()
conn.close()

