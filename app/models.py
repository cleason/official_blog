from django.db import models
from django.contrib.auth.models import User


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Configuration du site"

# Définition des statuts possibles pour un article
DRAFT = 'draft'
PUBLISHED = 'published'
STATUS_CHOICES = [
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),
]

class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Contenu")
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, verbose_name="Image")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Auteur")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT, verbose_name="Statut")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Article de blog"
        verbose_name_plural = "Articles de blog"

    def __str__(self):
        return self.title

# Modèle pour les annonces
class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    is_active = models.BooleanField(default=False, verbose_name="Actif")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Annonce"
        verbose_name_plural = "Annonces"

    def __str__(self):
        return self.title

# Modèle pour les commentaires
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments", verbose_name="Article")
    name = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    is_approved = models.BooleanField(default=True, verbose_name="Approuvé")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire de {self.author.username} sur {self.blog_post.title}"


# Models pour a propos de nous

class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    class Meta:
        ordering = ['-created_at']
        verbose_name = "A propos de nous"
        verbose_name_plural = "A propos de nous"
    def __str__(self):
        return self.title


# Models pour le temoignage
class Testimonial(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    is_active = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Temoignage"
        verbose_name_plural = "Temoignages"

    def __str__(self):
        return self.name


# Models pour contactez-nous
class ContactForm(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Nom de famille")
    last_name = models.CharField(max_length=50, verbose_name="Prénom")
    email = models.EmailField(verbose_name="Adresse e-mail")
    subject = models.CharField(max_length=100, verbose_name="Objet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    is_read = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Formulaire de contact"
        verbose_name_plural = "Formulaires de contact"

    def __str__(self):
        return self.name

class PageContent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre", blank=True)
    subtitle = models.CharField(max_length=255, verbose_name="Sous-titre", blank=True)
    content = models.TextField(verbose_name="Contenu", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création", blank=True)

    def __str__(self):
        return self.title
