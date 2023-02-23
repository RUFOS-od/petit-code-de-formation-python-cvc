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
// Récupération de toutes les tâches
$sql = "SELECT id, description, deadline FROM tasks";
$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
  // Affichage de toutes les tâches dans un tableau
  echo "<table><tr><th>ID</th><th>Description</th><th>Deadline</th><th>Action</th></tr>";
  while($row = mysqli_fetch_assoc($result)) {
    echo "<tr><td>".$row["id"]."</td><td>".$row["description"]."</td><td>".$row["deadline"]."</td><td><a href='update.php?id=".$row["id"]."'>Modifier</a> <a href='delete.php?id=".$row["id"]."'>Supprimer</a></td></tr>";
  }
  echo "</table>";
} else {
  echo "Aucune tâche trouvée.";
}
mysqli_close($conn);
?>