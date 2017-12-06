<!DOCTYPE html>
<html>
<head>
    <title>Vefverslun</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="css/shop.css">
    </head>
<body>
<h2>Veldu vöru sem þú vilt fá</h2>

<div class="myButt one">
    % for i in range(len(products)):
    <button class="">
    	
       <p> <a href="/cart/add/{{ products[i]["pid"] }}"> {{ products[i]["name"] }} </a> </p>
    </button>
    % end
</div>
<button class="mybutt one"><a href="/logout"> log out </a></button>


   
</body>
</html>