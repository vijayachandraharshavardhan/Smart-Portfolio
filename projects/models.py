from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    video = models.FileField(upload_to='projects/videos/', blank=True, null=True, help_text="Upload your project video (MP4, AVI, etc.)")
    position = models.PositiveIntegerField(default=0, help_text="Position for ordering (lower numbers appear first)")
    live_demo = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position', '-created_at']

    def __str__(self):
        return f"{self.position}. {self.title}"

class IntroVideo(models.Model):
    title = models.CharField(max_length=200, default="Intro Video")
    video_file = models.FileField(upload_to='videos/', help_text="Upload your intro video (MP4 format)")
    is_active = models.BooleanField(default=True, help_text="Only one active video will be displayed")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Intro Video"
        verbose_name_plural = "Intro Videos"

class Profile(models.Model):
    name = models.CharField(max_length=200, default="Vijaya Chandra Harsha Vardhan Battu")
    title = models.CharField(max_length=200, default="Full Stack Developer & Tech Enthusiast")
    about_me = models.TextField(default="Passionate full-stack developer with expertise in modern web technologies. I love creating innovative solutions and bringing ideas to life through code.")
    frontend_skills = models.TextField(default="React, Vue.js, HTML5, CSS3, JavaScript")
    backend_skills = models.TextField(default="Python, Django, Node.js, Express")
    database_skills = models.TextField(default="PostgreSQL, MongoDB, MySQL")
    tools_skills = models.TextField(default="Git, Docker, AWS, Linux")
    portfolio_description = models.TextField(default="Check out my latest projects")
    contact_description = models.TextField(default="Let's work together!")
    email = models.EmailField(default="your.email@example.com")
    linkedin = models.URLField(default="/in/yourprofile")
    github = models.URLField(default="/yourusername")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
