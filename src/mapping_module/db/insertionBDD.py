import sqlite3

conn = sqlite3.connect('WALL-E-Motion.db')
c = conn.cursor()

# Create table
c.execute('''INSERT INTO Properties VALUES ('1','240,100,50','800','90','Happy','31,100,50','Blue_Pink');''') #Blue
c.execute('''INSERT INTO Properties VALUES ('2','60,100,50','200','50','Sad','0,100,50','Yellow_Red');''') #Yellow
c.execute('''INSERT INTO Properties VALUES ('3','60,100,25','300','60','Surprised','0,100,50','Orange_Green');''') #Orange
c.execute('''INSERT INTO Properties VALUES ('4','120,100,50','500','70','Neutral','120,100,50','Green_Blue');''') #Green
c.execute('''INSERT INTO Properties VALUES ('5','0,100,50','600','80','Angry','31,100,50','Red_Yellow');''') #Red

c.execute('''INSERT INTO Animations VALUES ('1','happyanima','pathtoHappy','800','230');''')
c.execute('''INSERT INTO Animations VALUES ('2','sadanima','pathtoSad','200','150');''')
c.execute('''INSERT INTO Animations VALUES ('3','surprisedanima','pathtoSurprised','300','170');''')
c.execute('''INSERT INTO Animations VALUES ('4','neutralanima','pathtoNeutral','500','190');''')
c.execute('''INSERT INTO Animations VALUES ('5','angryanima','pathtoAngry','600','210');''')

c.execute('''INSERT INTO Emotions VALUES ('1','Happy','1','1');''')
c.execute('''INSERT INTO Emotions VALUES ('2','Sad','2','2');''')
c.execute('''INSERT INTO Emotions VALUES ('3','Suprised','3','3');''')
c.execute('''INSERT INTO Emotions VALUES ('4','Neutral','4','4');''')
c.execute('''INSERT INTO Emotions VALUES ('5','Angry','5','5');''')


# Save (commit) the changes
conn.commit()
conn.close()

