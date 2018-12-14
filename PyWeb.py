import cgi
import cgitb



import elements
import solver

form=cgi.FieldStorage()

value_set={}
test_value_set={}
'''
for item in elements.values:
    v=form.getvalue('R')
    test_value_set[item] = v if v is not None else ''
    value=int(v) if v is not None else None
    solver.set_value(item,value)


for item in elements.points:
    pt=form.getvalue('R')
    test_value_set[item] = pt if pt is not None else ''
    pt=eval(pt)
    if len(pt) is 2:
        solver.set_value(item,pt)


for item in elements.element:
    value_set[item]=solver.get_value(item)

svalue_set={}
for item in elements.element:
    if value_set[item] is not None:
        svalue_set[item]='value="%s"'%str(value_set[item])
    else:
        svalue_set[item]=''
    print(svalue_set[item])
'''

for item in elements.element:
    v=form.getvalue('R')
    test_value_set[item]='value="%s"'%v if v is not None else ''

web_page="""    

<html>
<head>
    <link rel="stylesheet"  type="text/css"  href="css/index_input.css"/>
    <link rel="stylesheet"  type="text/css"  href="css/index_text.css"/>
</head>
<body background="material/Background2_Flowers.png">
    <div class="img">
        <img src="material/geo.png">
    </div>
    
    <form action="index.html" method="post">
        <value class="Alpha">
            <input name="Alpha" {Alpha} type="text" placeholder="Alpha" id="Alpha">
        </value>
        <value class="Beta">
            <input name="Alpha" {Beta} type="text" placeholder="Beta" id="Beta">
        </value>
        <value class="Gamma">
            <input name="Alpha" {Gamma} type="text" placeholder="Gamma" id="Gamma">
        </value>

        <value class="C">
            <input name="C" {C} type="text" placeholder="C" id="C">
        </value>
        <value class="E">
            <input name="E" {E} type="text" placeholder="E" id="E">
        </value>
        <value class="D">
            <input name="D" {D} type="text" placeholder="D" id="D">
        </value>

        <value class="F">
            <input name="F" {F} type="text" placeholder="F" id="F">
        </value>
        <value class="I">
            <input name="I" {I} type="text" placeholder="I" id="I">
        </value>
        <value class="H">
            <input name="H" {H} type="text" placeholder="H" id="H">
        </value>
        <value class="G">
            <input name="G" {G} type="text" placeholder="G" id="G">
        </value>

        <value class="A">
            <input name="A" {A} type="text" placeholder="A" id="A">
        </value>
        <value class="R">
            <input name="R" {R} type="text" placeholder="R" id="R">
        </value>

        <value class="CE">
            <input name="CE" {CE} type="text" placeholder="CE" id="CE">
        </value>
        <value class="ED">
            <input name="ED" {ED} type="text" placeholder="ED" id="ED">
        </value>
        <value class="DC">
            <input name="DC" {DC} type="text" placeholder="DC" id="DC">
        </value>

        <value class="CF">
            <input name="CF" {CF} type="text" placeholder="CF" id="CF">
        </value>
        <value class="FE">
            <input name="FE" {FE} type="text" placeholder="FE" id="FE">
        </value>
        <value class="EI">
            <input name="EI" {EI} type="text" placeholder="EI" id="EI">
        </value>
        <value class="IH">
            <input name="IH" {IH} type="text" placeholder="IH" id="IH">
        </value>
        <value class="HD">
            <input name="HD" {HD} type="text" placeholder="HD" id="HD">
        </value>
        <value class="DG">
            <input name="DG" {DG} type="text" placeholder="DG" id="DG">
        </value>
        <value class="GC">
            <input name="GC" {GC} type="text" placeholder="GC" id="GC">
        </value>
        <value class="EH">
            <input name="EH" {EH} type="text" placeholder="EH" id="EH">
        </value>
        <value class="ID">
            <input name="ID" {ID} type="text" placeholder="ID" id="ID">
        </value>

        <value class="ARC1">
            <input name="ARC1" {ARC1} type="text" placeholder="ARC1" id="ARC1">
        </value>
        <value class="ARC2">
            <input name="ARC2" {ARC2} type="text" placeholder="ARC2" id="ARC2">
        </value>
        <value class="ARC3">
            <input name="ARC3" {ARC3} type="text" placeholder="ARC3" id="ARC3">
        </value>
        <value class="ARC4">
            <input name="ARC4" {ARC4} type="text" placeholder="ARC4" id="ARC4">
        </value>
        <value class="ARC5">
            <input name="ARC5" {ARC5} type="text" placeholder="ARC5" id="ARC5">
        </value>

        <value class="trianglearea">
            <input name="area_triangle" {area_triangle} type="text" placeholder="triangle" id="trianglearea">
        </value>
        <value class="circlearea">
            <input name="area_circle" {area_circle} type="text" placeholder="circlearea" id="circlearea">
        </value>
        <value class="S1">
            <input name="S1" {S1} type="text" placeholder="S1" id="S1">
        </value>
        <value class="S2">
            <input name="S2" {S2} type="text" placeholder="S2" id="S2">
        </value>
        <value class="S3">
            <input name="S3" {S3} type="text" placeholder="S3" id="S3">
        </value>
        <value class="S4">
            <input name="S4" {S4} type="text" placeholder="S4" id="S4">
        </value>
        <value class="S5">
            <input name="S5" {S5} type="text" placeholder="S5" id="S5">
        </value>
        <value class="S6">
            <input name="S6" {S6} type="text" placeholder="S6" id="S6">
        </value>

        <value class="trianglepmeter">
            <input name="perimeter_triangle" {perimeter_triangle} type="text" placeholder="triangle" id="trianglepmeter">
        </value>
        <value class="circlepmeter">
            <input name="perimeter_circle" {perimeter_circle} type="text" placeholder="value" id="circlepmeter">
        </value>

        <button type="submit">Solve</button>
    </form>
    
    <!
    /*****************************************************/
    /*****************************************************/
    /*****************************************************/
    /*****************************************************/
    /*****************************************************/
    >
    
    <value class="Alpha">
        <label for="Alpha">Alpha</label>
    </value>
    <value class="Beta">
        <label for="Beta">Alpha</label>
    </value>
    <value class="Gamma">
        <label for="Gamma">Gamma</label>
    </value>
    
    <value class="C">
        <label for="C">C</label>
    </value>
    <value class="E">
        <label for="E">E</label>
    </value>
    <value class="D">
        <label for="D">D</label>
    </value>
    
    <value class="F">
        <label for="F">F</label>
    </value>
    <value class="I">
        <label for="I">I</label>
    </value>
    <value class="H">
        <label for="H">H</label>
    </value>
    <value class="G">
        <label for="G">G</label>
    </value>
    
    <value class="A">
        <label for="A">A</label>
    </value>
    <value class="R">
        <label for="R">R</label>
    </value>
    
    <value class="CE">
        <label for="CE">CE</label>
    </value>
    <value class="ED">
        <label for="ED">ED</label>
    </value>
    <value class="DC">
        <label for="DC">DC</label>
    </value>
    
    <value class="CF">
        <label for="CF">CF</label>
    </value>
    <value class="FE">
        <label for="FE">FE</label>
    </value>
    <value class="EI">
        <label for="EI">EI</label>
    </value>
    <value class="IH">
        <label for="IH">IH</label>
    </value>
    <value class="HD">
        <label for="HD">HD</label>
    </value>
    <value class="DG">
        <label for="DG">DG</label>
    </value>
    <value class="GC">
        <label for="GC">GC</label>
    </value>
    <value class="EH">
        <label for="EH">EH</label>
    </value>
    <value class="ID">
        <label for="ID">ID</label>
    </value>
    
    <value class="ARC1">
        <label for="ARC1">ARC1</label>
    </value>
    <value class="ARC2">
        <label for="ARC2">ARC2</label>
    </value>
    <value class="ARC3">
        <label for="ARC3">ARC3</label>
    </value>
    <value class="ARC4">
        <label for="ARC4">ARC4</label>
    </value>
    <value class="ARC5">
        <label for="ARC5">ARC5</label>
    </value>
    
    <value class="trianglearea">
        <label for="trianglearea">Triangle Area</label>
    </value>
    <value class="circlearea">
        <label for="circlearea">Circle Area</label>
    </value>
    <value class="S1">
        <label for="S1">S1</label>
    </value>
    <value class="S2">
        <label for="S2">S2</label>
    </value>
    <value class="S3">
        <label for="S3">S3</label>
    </value>
    <value class="S4">
        <label for="S4">S4</label>
    </value>
    <value class="S5">
        <label for="S5">S5</label>
    </value>
    <value class="S6">
        <label for="S6">S6</label>
    </value>
    
    <value class="trianglepmeter">
        <label for="trianglepmeter">Triangle Perimeter</label>
    </value>
    <value class="circlepmeter">
        <label for="circlepmeter">Circle Perimeter</label>
    </value>
    
</body>
</html>

    """.format_map(test_value_set)

print(
    web_page
)

