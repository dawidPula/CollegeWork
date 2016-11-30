#!/usr/local/bin/python3

import cgi,cgitb  
cgitb.enable() 

print('Content-Type:text/html')
print()

self = <br>
form_data=cgi.FieldStorage()
if len(form_data)>0:
	ans1=set(form_data.getfirst('Q1'))
	ans2=set(form_data.getfirst('Q2'))
	ans3=set(form_data.getlist('Q3'))
	ans4=set(form_data.getlist('Q4'))
	vaild_ans={"a","b","c","d"}
	output =""
	result={"Q1":0,"Q2":0,"Q3":0,"Q4":0}
	marks=[]
	test= ans1|ans2|ans3|ans4
	if len(ans1) and len(ans2) and len(ans3) and len(ans4) >=1:
	        if test <= vaild_ans:
	                if ans1 <= {"b"}:
	                        result["Q1"]=1
	                if ans2 <= {"d"}:
	                        result["Q2"]=1
	                if ans3 <= {"a","c"}:
	                        result["Q3"]=1
	                if ans4 <= {"c"}:
	                        result["Q4"]=1
	                for i in sorted(result):
	                        if result[i] == 1:
	                                marks+=["&check;"]
	                        else:
	                                marks+=["&cross;"]
	                score=marks.count("&check;")
	                if score == 4:
	                        comment="You are a true Pokemon Master!!!!!!!!"
	                else:
	                        comment="Keep trining to become the very best !!!"
	                self="""<!DOCTYPE html>
			<html lang="en">
	        <head>
	        <title>PokeQuiz</title>
	        <style type="text/css">
			body{
	 		background: url("http://i265.photobucket.com/albums/ii220/ivnovitch/pokeball.png");
	    	margin:0px, auto;
	    	text-align: center;
			}
			table{
			background-color: #FFFFFF;
			width:200px;
			margin:auto;
			}
			h1{
			background-color: #FFFFFF;
			}
			p{
			background-color: #FFFFFF;
			}
			</style>
			<body>
			<h1>%s</h1>
			<table>
			<th>|Question|</th>
			<th>|Your Anwser|</th>
			<th>|Result|</th>
			<tr>
			<td>Q1</td>
			<td>%s</td>
			<td>%s</td>
			</tr>
			<tr>
			<td>Q2</td>
			<td>%s</td>
			<td>%s</td>
			</tr>
			<tr>
			<td>Q3</td>
			<td>%s</td>
			<td>%s</td>
			</tr>
			<tr>
			<td>Q4</td>
			<td>%s</td>
			<td>%s</td>
			</tr>
			<p>you scored %i out of 4!!!!</p>
			</table>
			</body>
				""" %(comment,str(ans1).strip("{}''"),marks[0],str(ans2).strip("{}''")\
					,marks[1],(str(ans3)).replace("{","").replace("}","").replace("'","")\
					,marks[2],(str(ans4)).replace("{","").replace("}","").replace("'","")\
					,marks[3],score)
	        else:
	                output="""<!DOCTYPE html>
			<html lang="en">
	    		<head>
	        	<title>PokeQuiz</title>
	    		</head>
	    		<body>
	    		<h1>ERROR DETECTED !!!CHEATER YOU WILL NEVER BECOME A POKEMON MASTER!!!!!"</h1>
	    		</body>"""
	else:
	        output"""<!DOCTYPE html>
	        <html lang="en">
	    	<head>
	        <title>PokeQuiz</title>
	    	</head>
	    	<body>
	    	<h1>ERROR DETECTED !!!please input data or you will never be
	    	a Pokemon Master!!!!!"</h1>
	    	</body>"""
output="""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PokeQuiz</title>
        <style type="text/css">
body 
{
  background: url("http://i265.photobucket.com/albums/ii220/ivnovitch/pokeball.png");
    margin:auto;
    text-align: center;
}
div{
    margin: auto;
    width: 500px;
}
#chick{
margin-left: 50px;
}
#button{
background-color: #E62E00;
color:#ffffff;
height: 50px;
width: 300px;
margin: auto;
}
FIELDSET{
  width: 500px;
  border:5px groove green;
  background-color:#ffffff 
}
legend {
    margin-left: 50px;
    width: 400px;
  border:5px ridge red;
  background-color:#ffffff ;
}
        </style>
    </head>
    <body>
    	<img alt="pokemon "id="pokemon" height="200" width="400"
    	src="http://img2.wikia.nocookie.net/__cb20130917213339/logopedia/images/f/f8/Pok%C3%A9mon_Gotta_Catch_%27Em_All_1.png">
    	<div><form action="quiz.py" method="get">
    		<FIELDSET>
    		<LEGEND>What pokemon is #257 in the pokedex?</LEGEND>
    		<input type="radio" name="Q1" value="a" id="a">
    		<label for="a">Mew</label><br>
    		<input type="radio" name="Q1" value="b" id="b">
    		<label for="b">Blaziken</label><br>
    		<input type="radio" name="Q1" value="c" id="c">
    		<label for="c">Wurmple</label><br>
    		</FIELDSET>
    			<FIELDSET>
    			<LEGEND>What pokemon do you help Wally catch on route 102 in <b>Pokemon Ruby /Sapphire&#169;</b></LEGEND>
    			<input type="radio" name="Q2" value="a" id="a2">
    			<label for="a2">Zigzagoon</label><br>
    			<input type="radio" name="Q2" value="b" id="b2">
    			<label for="b2">Poochyena</label><br>
    			<input type="radio" name="Q2" value="c" id="c2">
    			<label for="c2">Wurmple</label><br>
    			<input type="radio" name="Q2" value="d" id="d2">
    			<label for="d2">Ralts</label><br>
    			</FIELDSET>
    				<FIELDSET>
    				<LEGEND>Ghost type pokemon are immune to which types?
    				</LEGEND>
    				<input type="checkbox" name="Q3" value="a" id="a3">
    				<label for="a3">Normal</label><br>
    				<input type="checkbox" name="Q3" value="b" id="b3">
    				<label for="b3">Rock</label><br>
    				<input type="checkbox" name="Q3" value="c" id="c3">
    				<label for="c3">Fight</label><br>
    				</FIELDSET>
    					<FIELDSET>
    					<LEGEND>Whos this pokemon?</LEGEND>
    					<img id="chick"src="http://www.cubed3.com/media/2012/September/whodatpoke2.jpg"><br>
    					<input type="checkbox" name="Q4" value="a" id="a4">
    					<label for="a4">Oddish</label><br>
    					<input type="checkbox" name="Q4" value="b" id="b4">
    					<label for="b4">Bayleef</label><br>
    					<input type="checkbox" name="Q4" value="c" id="c4">
    					<label for="c4">Chikorita</label><br>
    					<input type="checkbox" name="Q4" value="d" id="d4">
    					<label for="d4">Grovyle</label><br>
    					</FIELDSET>
    					<input type="submit" id="button"
                        value="I CHOSE YOU PIKACHU !!!">
                        %s
    	</form></div>
    </body>""" %(self)
print(output)