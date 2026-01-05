# MegaKit

A modern, responsive website built with Django backend and Bootstrap frontend (Template), featuring user management, blogging capabilities, and a comprehensive website structure.

## Features

- **User Management**: Complete authentication system with login, signup, and password reset functionality
- **Blog System**: Full-featured blogging platform with rich text editing, categories, tags, comments, and search
- **Website Pages**: Professional landing pages including home, about, services, projects, and contact
- **Rich Text Editor**: Integrated Summernote editor with Bootstrap 4 theme for content creation
- **CAPTCHA Integration**: Multi-captcha support for enhanced security
- **SEO Optimization**: Built-in sitemaps and robots.txt for search engine optimization
- **Responsive Design**: Bootstrap-powered frontend that works seamlessly across all devices
- **Static File Management**: Compressed and optimized static assets for better performance
- **Admin Interface**: Customizable Django admin with multi-captcha support

## Tech Stack

### Backend

- **Django 5.2.7**: High-level Python web framework
- **Python 3.x**: Programming language
- **PostgreSQL/SQLite**: Database systems for data persistence (PostgreSQL for production, SQLite for development).
- **Additional Django Packages**:
  - django-taggit: For tagging functionality
  - django-summernote: Rich text editor integration
  - django-simple-captcha: CAPTCHA implementation
  - django-robots: Robots.txt management
  - django-compressor: Static file compression
  - django-extensions: Additional Django utilities

### Frontend

MegaKit Bootstrap template by [Themefisher](https://themefisher.com/) (Distributed by [Themewagon](https://themewagon.com))

## Minimum Requirements

- Python 3.13
- Django 5.2.7 (LTS)

The rest of needed libraries, frameworks & packages have been provided in `requirements.txt` file, which can be installed on the virtual machine by execution of the following command

```bash
pip install -r requirements.txt
```

## Configuration

### Development Settings

- Located in `megakit/settings/dev.py`
- Uses SQLite database (Django Default)
- Debug toolbar enabled

### Production Settings

- Located in `megakit/settings/prod.py`
- Uses PostgreSQL database

### Environment Variables

Configure the `.env` file, like the sample provided in the `.env.sample` file

## Project Structure

```
megakit/
├── accounts/          # User management app
├── blog/             # Blog functionality
├── website/          # Main website pages
├── megakit/          # Project settings
├── staticfiles/      # Static assets (CSS, JS, images)
├── templates/        # HTML templates
├── media/            # User-uploaded files
└── requirements.txt  # Python dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
