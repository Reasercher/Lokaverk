<!DOCTYPE html>
<html>
<head>
	<title>karfa</title>
    <link rel="stylesheet" type="text/css" href="css/shop.css">
</head>
<body>


<div class="mybutt one">
    <h1>Karfa</h1>
    % if len(karfa) <= 0:
        <p>Það eru engar vörur í körfu</p>
        <p><a href="/shop">Versla meira</a></p>
    % else:
        % for i in range(len(karfa)):
            <p> {{ karfa[i] }} <p>
        % end
    <p><a href="/shop">Versla meira</a></p>
    <p><a href="/cart/remove">Fjarlægum allar vörur úr körfu</a></p>
</div>

</body>
</html>