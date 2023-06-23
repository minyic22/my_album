from django.db import models


# Create your models here.
# CREATE TABLE image (
#     image_id SERIAL PRIMARY KEY,
#     image_url VARCHAR(255) NOT NULL,
#     upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# );
#
# CREATE TABLE tag (
#     tag_id SERIAL PRIMARY KEY,
#     tag_name VARCHAR(50) NOT NULL
# );
#
# CREATE TABLE image_tag (
#     image_id INT REFERENCES Image(image_id),
#     tag_id INT REFERENCES Tag(tag_id),
#     PRIMARY KEY (image_id, tag_id)
# );

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=255, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url

    class Meta:
        db_table = 'image'
        ordering = ['-upload_date']


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'tag'
        ordering = ['tag_name']


class ImageTag(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image_id) + ' ' + str(self.tag_id)

    class Meta:
        db_table = 'image_tag'
        ordering = ['image_id', 'tag_id']
