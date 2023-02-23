<?php
// Connexion à la base de données
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Vérification de la connexion
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
// Récupération de tous les messages
$sql = "SELECT message, sender FROM messages";
$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
  // Affichage de tous les messages dans une liste
  echo "<ul>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<li>".$row["sender"].": ".$row["message"]."</li>";
  }
  echo "</ul>";
} else {
  echo "Aucun message trouvé.";
}
mysqli_close($conn);