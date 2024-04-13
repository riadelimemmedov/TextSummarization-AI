from tortoise import fields, models


# !TextSummary
class TextSummary(models.Model):
    """
    TextSummary Model

    This code defines a Django model class named `TextSummary` with fields representing a URL, summary, and creation timestamp.

    Attributes:
    -----------
    - `url` (TextField): Represents the URL associated with the text summary.
    - `summary` (TextField): Represents the actual text summary.
    - `created_at` (DatetimeField): Represents the creation timestamp of the text summary.

    Methods:
    --------
    - `__str__(self)`: Returns a string representation of the `TextSummary` instance, which is the URL.

    """
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url