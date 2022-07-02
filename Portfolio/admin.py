from django.contrib import admin
from .models import Home, About, Service, Skill, Testimonial, Category, Portfolio, Article, ContactUs, Contact, Social_Profile
from django.utils.html import format_html


# 1 - Home Page 1 - Home Page 1 - Home Page 1 - Home Page 1 - Home Page
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title1','name','image_tag']
    readonly_fields= ['show_photo']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="75px" height="75px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'



# 2 - About Page 2 - About Page 2 - About Page 2 - About Page 2 - About Page
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ['image_tag']
    readonly_fields= ['show_photo']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="75px" height="75px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'


# 3 - Service Page 3 - Service Page 3 - Service Page 3 - Service Page 3 - Service Page
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']



# 4 - Category Page 4 - Category Page 4 - Category Page 4 - Category Page 4 - Category Page
admin.site.register(Category)


# 5 - Portfolio Page 5 - Portfolio Page 5 - Portfolio Page 5 - Portfolio Page 5 - Portfolio Page
@admin.register(Portfolio)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']
    readonly_fields= ['show_photo']
    list_filter = ['category']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="110px" height="50px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'


# 6 - Testimonial Page 6 - Testimonial Page 6 - Testimonial Page 6 - Testimonial Page 6 - Testimonial Page
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']
    readonly_fields= ['show_photo']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="75px" height="75px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'


#
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


# 7 - Contact Page 7 - Contact Page 7 - Contact Page 7 - Contact Page 7 - Contact Page
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','address','phone']
admin.site.register(Contact,ContactAdmin)


# 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','is_read']
    list_display_links = ['name']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['name','subject','message']
    readonly_fields = ['name','subject','email','message']

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
admin.site.register(ContactUs,ContactUsAdmin)

admin.site.register(Social_Profile)