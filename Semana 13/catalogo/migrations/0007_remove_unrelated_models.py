from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogo", "0006_producto_imagen"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(name="Cliente"),
                migrations.DeleteModel(name="Rol"),
                migrations.DeleteModel(name="TipoPago"),
            ],
        ),
    ]
