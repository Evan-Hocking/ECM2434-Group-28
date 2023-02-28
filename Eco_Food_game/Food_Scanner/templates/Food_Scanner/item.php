{% extends "Food_Scanner/base.html" %}
{% block content %}
    <?php
    $barcode = $_GET['barcodeNumber'];
    ?>
    <h1>Item Name</h1>
    <img id="itemImage" src="https://images.openfoodfacts.org/images/products/80177173/front_en.149.400.jpg" alt="Item image">
    <p id="scores">EcoScore:</p>
    <p id="scores">Energy per 100g:</p>
    <p id="scores">NutriScore:</p>
    <p id="scores">ProcessedScore:</p>
    <p id="scores">Points:</p>
{% endblock content%}