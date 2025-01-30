<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Calculator</title>
</head>
<body>
    <h2>Number Calculator</h2>
    <form action="process.php" method="POST">
        <div>
            <label for="a">Enter Value for a:</label>
            <input type="number" id="a" name="a" required/>
        </div>
        <div>
            <label for="b">Enter Value for b:</label>
            <input type="number" id="b" name="b" required/>
        </div>
        <div>
            <label for="c">Enter Value for c:</label>
            <input type="number" id="c" name="c" required/>
        </div>
        <button type="submit">Calculate</button>
    </form>
</body>
</html>