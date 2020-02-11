html = """
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <font color=red> @여기 </font>
    </body>
</html>
"""


html = html.replace('@여기', '반가워 나는 뽀로로야')
print(html)