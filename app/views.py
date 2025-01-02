from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContactForm
from .models import BlogPost, Announcement, PageContent, Testimonial
from .forms import TestimonialForm
from django.http import Http404, HttpResponse

def index(request):
    announcement = Announcement.objects.filter(is_active=True).first()
    page_content = PageContent.objects.first()
    posts_list = BlogPost.objects.filter(status='published')
    paginator = Paginator(posts_list, 8)  # Affiche 10 articles par page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'app/index.html', {
        'posts': posts,
        'announcement': announcement,
        'page_content': page_content
        })


def detail(request, post_id, slug):
    # Récupérer l'article
    post = get_object_or_404(BlogPost, pk=post_id, slug=slug)
    if post.status != "published":  # Remplacez "actif" par la valeur correspondant au statut actif dans vos `STATUS_CHOICES`
        raise Http404("L'article demandé n'existe pas.")
    
    # Récupérer les témoignages existants
    testimonials = Testimonial.objects.filter(is_active=True)

    # Initialiser le formulaire
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()
            return redirect('detail', post_id=post.id, slug=post.slug)  # Redirection après soumission
    else:
        form = TestimonialForm()

    return render(request, 'app/detail.html', {
        'post': post,
        'testimonials': testimonials,
        'form': form,
    })

def a_propos(request):
    return render(request, 'app/a_propos.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Créer une instance du formulaire de contact
        ContactForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        
        # Message de confirmation
        messages.success(request, "Votre message a été envoyé avec succès !")
        return redirect('contact')  # Redirige vers la page de contact ou une autre page
    return render(request, 'app/contact.html')



