import os
import gettext

# Set up localization
LOCALE_DIR = 'translations'
DOMAIN = 'messages'

def setup_locale(language='fr'):
    """Set up the translation for the specified language"""
    locale_path = os.path.join(LOCALE_DIR, language, 'LC_MESSAGES')
    translation = gettext.translation(DOMAIN, LOCALE_DIR, languages=[language], fallback=True)
    translation.install()
    return translation.gettext, translation.ngettext

def demo_english():
    """Demo with English (no translation)"""
    print("=== English Demo ===")
    
    def _(message):
        return message
    
    def ngettext_en(singular, plural, n):
        return singular if n == 1 else plural
    
    greeting = _("Hello, World!")
    print(greeting)
    
    for num in [1, 3]:
        message = ngettext_en(
            "You have one message", 
            "You have %(num)d messages", 
            num
        ) % {"num": num}
        print(message)

def demo_french():
    """Demo with French translations"""
    print("\n=== French Demo ===")
    
    # Set up French translations
    _, ngettext_fr = setup_locale('fr')
    
    # Get the translation function
    translation = gettext.translation(DOMAIN, LOCALE_DIR, languages=['fr'], fallback=True)
    _ = translation.gettext
    
    greeting = _("Hello, World!")
    print(greeting)
    
    for num in [1, 3]:
        message = ngettext_fr(
            "You have one message", 
            "You have %(num)d messages", 
            num
        ) % {"num": num}
        print(message)

if __name__ == "__main__":
    # Demo both languages
    demo_english()
    demo_french()