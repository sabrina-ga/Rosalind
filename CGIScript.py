#!/usr/bin/env python3

import cgi

# Content-Type für die Ausgabe
print("Content-Type: text/html")
print()

# Eingabedaten des Benutzers auslesen
form = cgi.FieldStorage()

# Überprüfen, ob ein Parameter übergeben wurde
name = form.getvalue("name", "Welt")

# HTML-Ausgabe
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI Example</title>
</head>
<body>
    <h1>Hallo, {name}!</h1>
    <form method="get" action="">
        <label for="name">Dein Name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Abschicken</button>
    </form>
</body>
</html>
""")
