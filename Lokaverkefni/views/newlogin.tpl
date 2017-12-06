<!DOCTYPE html>
<html> 
  <head>
    <meta charset="utf-8">
    <title>Innskrá</title>
    <link rel="stylesheet" type="text/css" href="css/shop.css">
  </head>
  <body>
    <div class="center">
      <form method='post' action='/donyskra'>
        <h2>Nýskráningarform:</h2>
        <h3>Notendanafn:</h3><br>
        <input type="text" name='user' required><br>
        <h3>Lykilorð:</h3><br>
        <input type="text" name='pass' required><br>
        <input type='submit' value='Innskrá'>
        <input type='reset' value='Hreinsa'>
      </form>
    </div>
  </body>
</html>