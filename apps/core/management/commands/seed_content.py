import sys
import os
from django.conf import settings

# Add project root to sys.path
sys.path.append(str(settings.BASE_DIR))

from django.core.management.base import BaseCommand
from apps.core.models import GlobalStyles
from apps.homepage_options.models import (
    HomePage, HomeHero, HomeIntro, HomeMission, HomeObjective, HomeMotto, HomeStat
)
from apps.about_options.models import (
    AboutPage, AboutHero, AboutIntro, AboutStat, AboutCore, AboutStrategic, AboutObjective
)
from apps.committee_options.models import (
    CommitteePage, CommitteeHero, CommitteeBoard, CommitteeMember, CommitteeSectionSettings
)
from apps.team_options.models import (
    TeamPage, TeamHero, TeamCoachesSettings, TeamPlayersSettings,
    Coach, Player, TeamPhotoSection, TeamCTA
)
from apps.membership_options.models import (
    MembershipPage, MembershipHero, MembershipBenefit, MembershipFormSettings
)
from apps.events_options.models import (
    EventsPage, EventsHero, EventsSettings, Event
)
from apps.news_options.models import (
    NewsPage, NewsHero, NewsSettings, NewsCategory, NewsArticle
)
from apps.gallery_options.models import (
    GalleryPage, GalleryHero, GalleryCategory, GalleryImage, GallerySettings
)
from apps.contact_options.models import (
    ContactPage, ContactHero, ContactInfo, ContactSocial, ContactSettings
)
from apps.navigation.models import NavigationItem, FooterSettings, NavigationSettings, FooterLink
from apps.media.models import Media

class Command(BaseCommand):
    help = 'Seeds the database with initial content matching the frontend structure'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # 1. Global Styles
        GlobalStyles.objects.update_or_create(
            id=1,
            defaults={
                'brand_name_ne': "नेपाल भलिबल क्लब",
                'brand_name_en': "Nepal Volleyball Club",
                'brand_name_de': "Nepal Volleyball Club",
                'brand_subtitle_ne': "हामबर्ग e.V.",
                'brand_subtitle_en': "Hamburg e.V.",
                'brand_subtitle_de': "Hamburg e.V.",
                'primary_500': "#DC143C",
                'primary_600': "#B21031",
                'secondary_500': "#003893",
                'accent_500': "#FACC15",
                'transition_duration': 300
            }
        )
        self.stdout.write(self.style.SUCCESS('GlobalStyles updated'))

        # 2. Navigation Items
        items = [
            {'order': 1, 'path': '/', 'label_ne': 'गृहपृष्ठ', 'label_en': 'Home', 'label_de': 'Startseite'},
            {'order': 2, 'path': '/about', 'label_ne': 'हाम्रो बारेमा', 'label_en': 'About Us', 'label_de': 'Über uns'},
            {'order': 3, 'path': '/committee', 'label_ne': 'कार्यसमिति', 'label_en': 'Committee', 'label_de': 'Vorstand'},
            {'order': 4, 'path': '/team', 'label_ne': 'टोली', 'label_en': 'Team', 'label_de': 'Team'},
            {'order': 5, 'path': '/membership', 'label_ne': 'सदस्यता', 'label_en': 'Membership', 'label_de': 'Mitgliedschaft'},
            {'order': 6, 'path': '/events', 'label_ne': 'कार्यक्रमहरू', 'label_en': 'Events', 'label_de': 'Veranstaltungen'},
            {'order': 7, 'path': '/notice', 'label_ne': 'सूचना', 'label_en': 'Notices', 'label_de': 'Mitteilungen'},
            {'order': 8, 'path': '/news', 'label_ne': 'समाचार', 'label_en': 'News', 'label_de': 'Neuigkeiten'},
            {'order': 9, 'path': '/gallery', 'label_ne': 'ग्यालरी', 'label_en': 'Gallery', 'label_de': 'Galerie'},
            {'order': 10, 'path': '/contact', 'label_ne': 'सम्पर्क', 'label_en': 'Contact', 'label_de': 'Kontakt'},
        ]
        for item in items:
            NavigationItem.objects.update_or_create(
                href=item['path'],
                defaults={
                    'order': item['order'],
                    'label_ne': item['label_ne'],
                    'label_en': item['label_en'],
                    'label_de': item['label_de'],
                    'is_active': True
                }
            )
        self.stdout.write(self.style.SUCCESS('Navigation items updated'))

        # 2.5 Navigation Settings (Logo & Brand)
        NavigationSettings.objects.update_or_create(
            id=1,
            defaults={
                'brand_name_main_ne': "नेपाल भलिबल",
                'brand_name_main_en': "Nepal Volleyball",
                'brand_name_main_de': "Nepal Volleyball",
                'brand_name_secondary_ne': "क्लब हामबर्ग e.V.",
                'brand_name_secondary_en': "Club Hamburg e.V.",
                'brand_name_secondary_de': "Club Hamburg e.V.",
                'status': 'published'
            }
        )
        self.stdout.write(self.style.SUCCESS('NavigationSettings updated'))

        # 3. Home Page
        home_page, _ = HomePage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_en': "Nepal Volleyball Club Hamburg e.V.",
                'meta_description_en': "Official website of Nepal Volleyball Club Hamburg e.V."
            }
        )

        HomeHero.objects.update_or_create(
            page=home_page,
            defaults={
                'title_ne': 'नेपाल भलिबल क्लब हामबर्ग e.V.',
                'title_en': 'Nepal Volleyball Club Hamburg e.V.',
                'title_de': 'Nepal Volleyball Club Hamburg e.V.',
                'subtitle_ne': 'खेलकुदमार्फत नेपाली समुदायलाई एकताबद्ध गर्दै',
                'subtitle_en': 'Uniting the community through sports and culture',
                'subtitle_de': 'Einheit und Kultur durch Sport',
                'cta_join_label_ne': 'सदस्य बन्नुहोस्',
                'cta_join_label_en': 'Join Now',
                'cta_join_label_de': 'Mitglied werden',
                'cta_learn_label_ne': 'थप जान्नुहोस्',
                'cta_learn_label_en': 'Learn More',
                'cta_learn_label_de': 'Mehr erfahren',
            }
        )

        HomeMotto.objects.update_or_create(
            page=home_page,
            defaults={
                'text_ne': 'एकता, ऊर्जा र उत्साह — स्वास्थ्य, मित्रता र नेपाली कला–संस्कृति संरक्षण हाम्रो लक्ष्य',
                'text_en': 'Unity, Energy and Enthusiasm — Health, Friendship and Preservation of Nepali Culture',
                'text_de': 'Einheit, Energie und Begeisterung – Gesundheit, Freundschaft und Erhalt der nepalesischen Kultur',
                'button_label_ne': 'सम्पर्क गर्नुहोस्',
                'button_label_en': 'Contact Us',
                'button_label_de': 'Kontaktieren Sie uns',
            }
        )
            
        HomeIntro.objects.update_or_create(
            page=home_page,
            defaults={
                'mini_header_ne': 'हाम्रो बारेमा',
                'mini_header_en': 'About Us',
                'mini_header_de': 'Über uns',
                'title_ne': 'परिचय',
                'title_en': 'About Us',
                'title_de': 'Über uns',
                'text_ne': 'नेपाल भलिबल क्लब हामबर्ग e.V. जर्मनीको हामबर्गमा स्थापित एक गैर-नाफामुखी, सामाजिक तथा खेलकुद संस्था हो। यो क्लब जर्मनीमा रहेका नेपाली तथा अन्य इच्छुक समुदायलाई भलिबल खेलमार्फत एकताबद्ध गर्दै स्वास्थ्य, मित्रता, सामाजिक सद्भाव तथा नेपाली कला–संस्कृति र पहिचानको संरक्षण तथा प्रवर्द्धन गर्ने उद्देश्यले स्थापना गरिएको हो।',
                'text_en': 'Nepal Volleyball Club Hamburg e.V. is a non-profit sports and social organization based in Hamburg, Germany. Established to unite the Nepali community and others through volleyball, we aim to promote health, friendship, social harmony, and preserve Nepali art and culture.',
                'text_de': 'Der Nepal Volleyball Club Hamburg e.V. ist ein gemeinnütziger Sport- und Kulturverein mit Sitz in Hamburg, Deutschland. Unser Ziel ist es, durch Volleyballsport die nepalesische Gemeinschaft sowie interessierte Menschen zusammenzubringen, Gesundheit, Freundschaft und Teamgeist zu fördern sowie die nepalesische Kultur und Identität zu bewahren.',
                'subtext_ne': 'हाम्रो क्लब खेलकुदलाई माध्यम बनाएर समुदायबीच आपसी सहयोग, अनुशासन, नेतृत्व विकास र सकारात्मक सोचको विकास गर्दै स्वस्थ समाज निर्माणमा प्रतिबद्ध छ।',
                'subtext_en': 'We are committed to building a healthy society by fostering cooperation, discipline, leadership, and positive thinking through sports.',
                'subtext_de': 'Wir nutzen den Sport als Brücke für Integration, Zusammenhalt und soziale Entwicklung.',
            }
        )
            
        mission, _ = HomeMission.objects.update_or_create(
            page=home_page,
            defaults={
                'mission_label_ne': 'हाम्रो मिशन',
                'mission_label_en': 'Our Mission',
                'mission_label_de': 'Unsere Mission',
                'title_ne': 'हाम्रो उद्देश्यहरू',
                'title_en': 'Our Objectives',
                'title_de': 'Unsere Ziele',
                'description_ne': 'पूर्ण विवरण हेर्न स्वाइप गर्नुहोस्',
                'description_en': 'Swipe to explore our full vision.',
                'description_de': 'Wischen Sie, um unsere Vision zu erkunden.',
            }
        )

        objectives_list=[
            {"badge": "01", "text_ne": "भलिबल खेलको प्रवर्द्धन र विकास गर्नु", "text_en": "Promote and develop volleyball", "text_de": "Förderung des Volleyballsports"},
            {"badge": "02", "text_ne": "जर्मनीमा रहेका नेपालीहरूलाई एकताबद्ध गर्नु", "text_en": "Unite Nepalese in Germany", "text_de": "Stärkung der Einheit der nepalesischen Gemeinschaft"},
            {"badge": "03", "text_ne": "स्वास्थ्य, मित्रता र खेल भावना विकास गर्नु", "text_en": "Foster health, friendship and sportsmanship", "text_de": "Förderung von Gesundheit, Freundschaft und Teamgeist"},
            {"badge": "04", "text_ne": "युवा पुस्तालाई खेलकुदमा आकर्षित गर्नु", "text_en": "Attract youth to sports", "text_de": "Motivation der Jugend zum Sport"},
        ]

        # Use index as a unique identifier for objectives in a mission
        for i, obj in enumerate(objectives_list):
            HomeObjective.objects.update_or_create(
                mission=mission,
                order=i,
                defaults={
                    'badge_number': obj['badge'],
                    'text_ne': obj['text_ne'],
                    'text_en': obj['text_en'],
                    'text_de': obj['text_de'],
                }
            )

        stats_list = [
            {'label_ne': 'सदस्यहरू', 'label_en': 'Members', 'label_de': 'Mitglieder', 'value': 50},
            {'label_ne': 'कार्यक्रमहरू', 'label_en': 'Events', 'label_de': 'Events', 'value': 25},
            {'label_ne': 'वर्ष', 'label_en': 'Years', 'label_de': 'Jahre', 'value': 5},
            {'label_ne': 'पुरस्कारहरू', 'label_en': 'Awards', 'label_de': 'Auszeichnungen', 'value': 10},
        ]
        
        for i, stat in enumerate(stats_list):
            HomeStat.objects.update_or_create(
                page=home_page,
                order=i,
                defaults={
                    'label_ne': stat['label_ne'],
                    'label_en': stat['label_en'],
                    'label_de': stat['label_de'],
                    'value': stat['value'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Home Page content updated'))

        # 4. About Page
        about_page, _ = AboutPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_en': "About Us - Nepal Volleyball Club Hamburg e.V.",
                'meta_description_en': "Learn about our history, mission and values."
            }
        )

        AboutHero.objects.update_or_create(
            page=about_page,
            defaults={
                'since_text_ne': "२०२० देखि • हामबर्ग",
                'since_text_en': "Since 2020 • Hamburg",
                'since_text_de': "Seit 2020 • Hamburg",
                'show_pulsing_dot': True,
                'title_ne': "हाम्रो बारेमा",
                'title_en': "About Us",
                'title_de': "Über uns",
                'text_ne': "नेपाल भलिबल क्लब हामबर्ग e.V. जर्मनीको हामबर्गमा स्थापित एक गैर-नाफामुखी खेलकुद संस्था हो।",
                'text_en': "Nepal Volleyball Club Hamburg e.V. is a non-profit sports organization based in Hamburg, Germany.",
                'text_de': "Der Nepal Volleyball Club Hamburg e.V. ist ein gemeinnütziger Sportverein in Hamburg.",
                'background_color': "#030712"
            }
        )

        about_intro, _ = AboutIntro.objects.update_or_create(
            page=about_page,
            defaults={
                'title_part1_ne': "भलिबल क्लब",
                'title_part1_en': "More Than Just",
                'title_part1_de': "Mehr als nur",
                'title_part2_ne': "भन्दा बढी",
                'title_part2_en': "A Volleyball Club",
                'title_part2_de': "ein Volleyballverein",
                'text1_ne': "नेपाल भलिबल क्लब हामबर्ग e.V. जर्मनीको हामबर्गमा स्थापित एक गैर-नाफामुखी, सामाजिक तथा खेलकुद संस्था हो। यो क्लब जर्मनीमा रहेका नेपाली तथा अन्य इच्छुक समुदायलाई भलिबल खेलमार्फत एकताबद्ध गर्दै स्वास्थ्य, मित्रता, सामाजिक सद्भाव तथा नेपाली कला–संस्कृति र पहिचानको संरक्षण तथा प्रवर्द्धन गर्ने उद्देश्यले स्थापना गरिएको हो।",
                'text1_en': "Nepal Volleyball Club Hamburg e.V. is a non-profit sports and social organization based in Hamburg, Germany. Established to unite the Nepali community and others through volleyball, we aim to promote health, friendship, social harmony, and preserve Nepali art and culture.",
                'text1_de': "Der Nepal Volleyball Club Hamburg e.V. ist ein gemeinnütziger Sport- und Kulturverein mit Sitz in Hamburg, Deutschland. Unser Ziel ist es, durch Volleyballsport die nepalesische Gemeinschaft sowie interessierte Menschen zusammenzubringen, Gesundheit, Freundschaft und Teamgeist zu fördern sowie die nepalesische Kultur und Identität zu bewahren.",
                'text2_ne': "हाम्रो क्लब खेलकुदलाई माध्यम बनाएर समुदायबीच आपसी सहयोग, अनुशासन, नेतृत्व विकास र सकारात्मक सोचको विकास गर्दै स्वस्थ समाज निर्माणमा प्रतिबद्ध छ।",
                'text2_en': "We are committed to building a healthy society by fostering cooperation, discipline, leadership, and positive thinking through sports.",
                'text2_de': "Wir engagieren uns für den Aufbau einer gesunden Gesellschaft, indem wir Zusammenarbeit, Disziplin, Führungsqualitäten und positives Denken durch Sport fördern.",
                'established_label_ne': "स्थापना",
                'established_label_en': "Established",
                'established_label_de': "Gegründet",
                'established_year': "2020"
            }
        )

        about_stats = [
            {'label_ne': 'खेलाडीहरू', 'label_en': 'Players', 'label_de': 'Spieler', 'value': '50+'},
            {'label_ne': 'कार्यक्रमहरू', 'label_en': 'Events', 'label_de': 'Events', 'value': '20+'},
            {'label_ne': 'जोश', 'label_en': 'Passion', 'label_de': 'Leidenschaft', 'value': '100%'},
        ]
        for i, stat in enumerate(about_stats):
            AboutStat.objects.update_or_create(
                intro=about_intro,
                order=i,
                defaults={
                    'label_ne': stat['label_ne'],
                    'label_en': stat['label_en'],
                    'label_de': stat['label_de'],
                    'value': stat['value'],
                }
            )

        AboutCore.objects.update_or_create(
            page=about_page,
            defaults={
                'title_ne': "हाम्रो मूल मन्त्र",
                'title_en': "Our Core",
                'title_de': "Unser Kern",
                'vision_title_ne': "हाम्रो दृष्टिकोण",
                'vision_title_en': "Our Vision",
                'vision_title_de': "Unsere Vision",
                'vision_text_ne': "जर्मनीमा रहेका नेपालीहरूलाई भलिबल खेलमार्फत एकताबद्ध गर्दै एक स्वस्थ, सक्रिय र समृद्ध नेपाली समुदायको निर्माण गर्ने।",
                'vision_text_en': "To build a healthy, active and prosperous Nepali community by uniting Nepalese in Germany through volleyball.",
                'vision_text_de': "Aufbau einer gesunden, aktiven und wohlhabenden nepalesischen Gemeinschaft in Deutschland durch Volleyball.",
                'vision_icon': "Eye",
                'mission_title_ne': "हाम्रो मिशन",
                'mission_title_en': "Our Mission",
                'mission_title_de': "Unsere Mission",
                'mission_text_ne': "भलिबल खेलको प्रवर्द्धन गर्दै समुदायमा स्वास्थ्य, अनुशासन, टोली भावना र नेतृत्व क्षमताको विकास गर्ने।",
                'mission_text_en': "To develop health, discipline, team spirit and leadership skills in the community while promoting volleyball.",
                'mission_text_de': "Förderung von Gesundheit, Disziplin, Teamgeist und Führungskompetenz in der Gemeinschaft durch Volleyball.",
                'mission_icon': "Target"
            }
        )

        about_strategic, _ = AboutStrategic.objects.update_or_create(
            page=about_page,
            defaults={
                'strategic_title_ne': "रणनीतिक लक्ष्यहरू",
                'strategic_title_en': "Strategic Goals",
                'strategic_title_de': "Strategische Ziele",
                'objectives_title_ne': "हाम्रो उद्देश्यहरू",
                'objectives_title_en': "Our Objectives",
                'objectives_title_de': "Unsere Ziele",
                'promo_title_ne': "विश्वस्तरीय मापदण्ड",
                'promo_title_en': "Global Standards",
                'promo_title_de': "Globale Standards",
                'promo_text_ne': "हामबर्गमा अन्तर्राष्ट्रिय भलिबल उत्कृष्टता ल्याउँदै।",
                'promo_text_en': "Bringing international volleyball excellence to Hamburg.",
                'promo_text_de': "Internationale Volleyball-Exzellenz nach Hamburg bringen.",
                'promo_icon': "Globe"
            }
        )

        about_objectives = [
            {"text_ne": "भलिबल खेलको प्रवर्द्धन र विकास गर्नु", "text_en": "Promote and develop volleyball", "text_de": "Förderung des Volleyballsports"},
            {"text_ne": "जर्मनीमा रहेका नेपालीहरूलाई एकताबद्ध गर्नु", "text_en": "Unite Nepalese in Germany", "text_de": "Stärkung der Einheit der nepalesischen Gemeinschaft"},
            {"text_ne": "स्वास्थ्य, मित्रता र खेल भावना विकास गर्नु", "text_en": "Foster health, friendship and sportsmanship", "text_de": "Förderung von Gesundheit, Freundschaft and Teamgeist"},
            {"text_ne": "युवा पुस्तालाई खेलकुदमा आकर्षित गर्नु", "text_en": "Attract youth to sports", "text_de": "Motivation der Jugend zum Sport"},
            {"text_ne": "नेपाली कला, संस्कृति र पहिचानको संरक्षण गर्नु", "text_en": "Preserve Nepali art, culture and identity", "text_de": "Erhalt der nepalesischen Kultur und Identität"},
            {"text_ne": "राष्ट्रिय तथा अन्तर्राष्ट्रिय प्रतियोगितामा सहभागिता जनाउनु", "text_en": "Participate in national and international competitions", "text_de": "Teilnahme an regionalen und internationalen Wettbewerben"},
            {"text_ne": "सामाजिक र सामुदायिक कार्यक्रम आयोजना गर्नु", "text_en": "Organize social and community events", "text_de": "Organisation sozialer und kultureller Veranstaltungen"},
        ]
        for i, obj in enumerate(about_objectives):
            AboutObjective.objects.update_or_create(
                strategic=about_strategic,
                order=i,
                defaults={
                    'text_ne': obj['text_ne'],
                    'text_en': obj['text_en'],
                    'text_de': obj['text_de'],
                }
            )

        self.stdout.write(self.style.SUCCESS('About Page content updated'))

        # 5. Footer Content
        footer_settings, _ = FooterSettings.objects.update_or_create(
            id=1,
            defaults={
                'brand_name_main_ne': "नेपाल भलिबल",
                'brand_name_main_en': "Nepal Volleyball",
                'brand_name_main_de': "Nepal Volleyball",
                'brand_name_secondary_ne': "क्लब हामबर्ग e.V.",
                'brand_name_secondary_en': "Club Hamburg e.V.",
                'brand_name_secondary_de': "Club Hamburg e.V.",
                'description_ne': "हाम्रो क्लब खेलकुदलाई माध्यम बनाएर समुदायबीच आपसी सहयोग, अनुशासन, नेतृत्व विकास र सकारात्मक सोचको विकास गर्दै स्वस्थ समाज निर्माणमा प्रतिबद्ध छ।",
                'description_en': "We are committed to building a healthy society by fostering cooperation, discipline, leadership, and positive thinking through sports.",
                'description_de': "Wir nutzen den Sport als Brücke für Integration, Zusammenhalt und soziale Entwicklung.",
                'facebook_url': "https://facebook.com/volleyballnepal",
                'instagram_url': "https://instagram.com/volleyballnepal",
                'youtube_url': "https://youtube.com/volleyballnepal",
                'quick_links_title_ne': "छिटो लिंक",
                'quick_links_title_en': "Quick Links",
                'quick_links_title_de': "Quick Links",
                'contact_info_title_ne': "सम्पर्क",
                'contact_info_title_en': "Contact",
                'contact_info_title_de': "Kontakt",
                'address_ne': "Hellkamp 30, 20255 Hamburg, Germany",
                'address_en': "Hellkamp 30, 20255 Hamburg, Germany",
                'address_de': "Hellkamp 30, 20255 Hamburg, Germany",
                'phone': "+49 160 8176707",
                'email': "nvchdeutschland@gmail.com",
                'registered_info': "Registered: VR 26187 (e.V.)",
                'membership_title_ne': "सदस्यता",
                'membership_title_en': "Membership",
                'membership_title_de': "Mitgliedschaft",
                'membership_description_ne': "आजै सदस्य बन्नुहोस् र हाम्रो समुदायको हिस्सा बन्नुहोस्।",
                'membership_description_en': "Become a member today and part of our community.",
                'membership_description_de': "Werden Sie noch heute Mitglied und Teil unserer Gemeinschaft.",
                'membership_button_text_ne': "Join Now",
                'membership_button_text_en': "Join Now",
                'membership_button_text_de': "Mitglied werden",
                'copyright_text_ne': "© [year] Nepal Volleyball Club Hamburg e.V.",
                'copyright_text_en': "© [year] Nepal Volleyball Club Hamburg e.V.",
                'copyright_text_de': "© [year] Nepal Volleyball Club Hamburg e.V.",
                'privacy_label_ne': "Privacy Policy",
                'privacy_label_en': "Privacy Policy",
                'privacy_label_de': "Datenschutz",
                'terms_label_ne': "Terms of Service",
                'terms_label_en': "Terms of Service",
                'terms_label_de': "AGB",
                'status': 'published'
            }
        )

        # Footer Links
        links = [
            {'order': 1, 'url': '/', 'label_ne': 'गृहपृष्ठ', 'label_en': 'Home', 'label_de': 'Startseite'},
            {'order': 2, 'url': '/about', 'label_ne': 'हाम्रो बारेमा', 'label_en': 'About Us', 'label_de': 'Über uns'},
            {'order': 3, 'url': '/events', 'label_ne': 'कार्यक्रमहरू', 'label_en': 'Events', 'label_de': 'Veranstaltungen'},
            {'order': 4, 'url': '/news', 'label_ne': 'समाचार', 'label_en': 'News', 'label_de': 'Neuigkeiten'},
            {'order': 5, 'url': '/contact', 'label_ne': 'सम्पर्क', 'label_en': 'Contact', 'label_de': 'Kontakt'},
        ]
        for link in links:
            FooterLink.objects.update_or_create(
                footer=footer_settings,
                url=link['url'],
                defaults={
                    'order': link['order'],
                    'label_ne': link['label_ne'],
                    'label_en': link['label_en'],
                    'label_de': link['label_de']
                }
            )
        self.stdout.write(self.style.SUCCESS('Footer links updated'))

        # 03. Committee Page
        committee_page, _ = CommitteePage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'कार्यसमिति - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Committee - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Vorstand - Nepal Volleyball Club Hamburg e.V.',
                'meta_description_ne': 'नेपाल भलिबल क्लब हामबर्ग e.V. को कार्यसमिति सदस्यहरू',
                'meta_description_en': 'Committee members of Nepal Volleyball Club Hamburg e.V.',
                'meta_description_de': 'Vorstandsmitglieder von Nepal Volleyball Club Hamburg e.V.',
            }
        )

        CommitteeHero.objects.update_or_create(
            page=committee_page,
            defaults={
                'title_ne': 'हाम्रो नेतृत्व',
                'title_en': 'Our Leadership',
                'title_de': 'Unsere Führung',
                'subtitle_ne': 'क्लबको विकास र सञ्चालनका लागि समर्पित कार्यसमिति सदस्यहरू।',
                'subtitle_en': 'Dedicated executive committee members for the development and operation of the club.',
                'subtitle_de': 'Engagierte Vorstandsmitglieder für die Entwicklung und Leitung des Vereins.',
                'background_color': '#030712'
            }
        )

        CommitteeBoard.objects.update_or_create(
            page=committee_page,
            defaults={
                # President
                'pres_name': 'प्रेमकुमार शेरचन',
                'pres_role_ne': 'अध्यक्ष',
                'pres_role_en': 'President',
                'pres_role_de': 'Präsident',
                'pres_desc_ne': 'क्लबको समग्र नेतृत्व, नीति निर्माण तथा बाह्य प्रतिनिधित्व',
                'pres_desc_en': 'Overall leadership, policy making and external representation',
                'pres_desc_de': 'Gesamtleitung und Vertretung des Vereins',
                'pres_email': 'president@nepalvolleyball.de',
                
                # Secretary
                'sec_name': 'शिव प्रसाद अधिकारी',
                'sec_role_ne': 'सचिव',
                'sec_role_en': 'Secretary',
                'sec_role_de': 'Sekretär',
                'sec_desc_ne': 'प्रशासनिक कार्य, बैठक व्यवस्थापन तथा अभिलेख राख्ने',
                'sec_desc_en': 'Administrative tasks, meeting management and record keeping',
                'sec_desc_de': 'Verwaltung, Dokumentation und Organisation der Sitzungen',
                'sec_email': 'secretary@nepalvolleyball.de',
                
                # Treasurer
                'tres_name': 'तेज कुमार राई',
                'tres_role_ne': 'कोषाध्यक्ष',
                'tres_role_en': 'Treasurer',
                'tres_role_de': 'Schatzmeister',
                'tres_desc_ne': 'आर्थिक व्यवस्थापन, बजेट तथा लेखा–जोखा',
                'tres_desc_en': 'Financial management, budgeting and accounting',
                'tres_desc_de': 'Finanzverwaltung und Buchhaltung',
                'tres_email': 'treasurer@nepalvolleyball.de',
            }
        )

        CommitteeSectionSettings.objects.update_or_create(
            page=committee_page,
            defaults={
                'member_section_title_ne': 'कार्यसमिति सदस्यहरू',
                'member_section_title_en': 'Committee Members',
                'member_section_title_de': 'Vorstandsmitglieder'
            }
        )

        # General Members - For these we might want to clear and re-add or match by name
        # Actually, since it's a seed, we'll maintain the list
        general_names = [
            'Hari Bhandari', 'Hasta Thapa Magar', 'Hari Thapa Magar', 
            'Bijay Khadka', 'Bijay Gurung', 'Bhakta Pakhrin', 
            'Padam Sundar Shrestha', 'Gautam Shahi', 'Bel Gurung'
        ]
        
        # Simple approach: clear members for this page and re-add to ensure exact order/list
        CommitteeMember.objects.filter(page=committee_page).delete()
        for i, name in enumerate(general_names):
            CommitteeMember.objects.create(
                page=committee_page,
                name=name,
                order=i + 10
            )

        self.stdout.write(self.style.SUCCESS('Committee Page content updated'))

        # 04. Team Page
        team_page, _ = TeamPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'हाम्रो टोली - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Our Team - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Unser Team - Nepal Volleyball Club Hamburg e.V.',
                'meta_description_en': 'Meet our dedicated players and experienced coaches.',
            }
        )

        TeamHero.objects.update_or_create(
            page=team_page,
            defaults={
                'title_ne': 'हाम्रो टोली',
                'title_en': 'Our Team',
                'title_de': 'Unser Team',
                'text_ne': 'समर्पित खेलाडी र अनुभवी प्रशिक्षकहरूको टोली जसले क्लबको सफलताको निम्ति निरन्तर मेहनत गरिरहेका छन्।',
                'text_en': 'A team of dedicated players and experienced coaches working tirelessly for the club\'s success.',
                'text_de': 'Ein Team aus engagierten Spielern und erfahrenen Trainern, die unermüdlich für den Erfolg des Vereins arbeiten.',
                'image_url': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?w=1600&q=80'
            }
        )

        TeamCoachesSettings.objects.update_or_create(
            page=team_page,
            defaults={
                'title_ne': 'प्रशिक्षक टोली',
                'title_en': 'Coaching Team',
                'title_de': 'Trainerteam',
            }
        )

        TeamPlayersSettings.objects.update_or_create(
            page=team_page,
            defaults={
                'title_ne': 'हाम्रा खेलाडीहरू',
                'title_en': 'Our Players',
                'title_de': 'Unsere Spieler',
            }
        )

        coaches_data = [
            {
                'name_ne': 'कृष्ण बहादुर थापा', 'name_en': 'Krishna Bahadur Thapa', 'name_de': 'Krishna Bahadur Thapa',
                'role_ne': 'मुख्य प्रशिक्षक', 'role_en': 'Head Coach', 'role_de': 'Cheftrainer',
                'experience_ne': '१५ वर्ष अनुभव', 'experience_en': '15 Years Experience', 'experience_de': '15 Jahre Erfahrung'
            },
            {
                'name_ne': 'रमेश अधिकारी', 'name_en': 'Ramesh Adhikari', 'name_de': 'Ramesh Adhikari',
                'role_ne': 'सहायक प्रशिक्षक', 'role_en': 'Assistant Coach', 'role_de': 'Assistenztrainer',
                'experience_ne': '८ वर्ष अनुभव', 'experience_en': '8 Years Experience', 'experience_de': '8 Jahre Erfahrung'
            }
        ]
        
        Coach.objects.filter(page=team_page).delete()
        for i, coach in enumerate(coaches_data):
            Coach.objects.create(
                page=team_page,
                order=i,
                **coach
            )

        players_data = [
            {'name_ne': 'राज गुरुङ', 'name_en': 'Raj Gurung', 'name_de': 'Raj Gurung', 'number': '1', 'pos_ne': 'सेट्टर', 'pos_en': 'Setter', 'pos_de': 'Zuspieler'},
            {'name_ne': 'सन्तोष तामाङ', 'name_en': 'Santosh Tamang', 'name_de': 'Santosh Tamang', 'number': '7', 'pos_ne': 'अउटसाइड हिटर', 'pos_en': 'Outside Hitter', 'pos_de': 'Außenangreifer'},
            {'name_ne': 'बिशाल मगर', 'name_en': 'Bishal Magar', 'name_de': 'Bishal Magar', 'number': '10', 'pos_ne': 'मिडल ब्लकर', 'pos_en': 'Middle Blocker', 'pos_de': 'Mittelblocker'},
            {'name_ne': 'अर्जुन राई', 'name_en': 'Arjun Rai', 'name_de': 'Arjun Rai', 'number': '5', 'pos_ne': 'लिबेरो', 'pos_en': 'Libero', 'pos_de': 'Libero'},
            {'name_ne': 'दिपक श्रेष्ठ', 'name_en': 'Deepak Shrestha', 'name_de': 'Deepak Shrestha', 'number': '9', 'pos_ne': 'अपोजिट', 'pos_en': 'Opposite', 'pos_de': 'Diagonalangreifer'},
            {'name_ne': 'सुमन पोखरेल', 'name_en': 'Suman Pokharel', 'name_de': 'Suman Pokharel', 'number': '12', 'pos_ne': 'अउटसाइड हिटर', 'pos_en': 'Outside Hitter', 'pos_de': 'Außenangreifer'},
        ]

        Player.objects.filter(page=team_page).delete()
        for i, player in enumerate(players_data):
            Player.objects.create(
                page=team_page,
                order=i,
                name_ne=player['name_ne'],
                name_en=player['name_en'],
                name_de=player['name_de'],
                number=player['number'],
                position_ne=player['pos_ne'],
                position_en=player['pos_en'],
                position_de=player['pos_de']
            )

        TeamPhotoSection.objects.update_or_create(
            page=team_page,
            defaults={
                'title_ne': 'टोली फोटो',
                'title_en': 'Team Photo',
                'title_de': 'Teamfoto',
                'subtitle_ne': '२०२६ को आधिकारिक टोली फोटो',
                'subtitle_en': 'Official Team Photo 2026',
                'subtitle_de': 'Offizielles Teamfoto 2026',
                'image_url': 'https://images.unsplash.com/photo-1577223625816-7546f13df25d?w=1200&q=80'
            }
        )

        TeamCTA.objects.update_or_create(
            page=team_page,
            defaults={
                'title_ne': 'टोलीमा सामेल हुनुहोस्',
                'title_en': 'Join the Team',
                'title_de': 'Werde Teil des Teams',
                'text_ne': 'भलिबल खेल्न चाहनुहुन्छ? हामीसँग जोडिनुहोस्!',
                'text_en': 'Want to play volleyball? Join us!',
                'text_de': 'Möchtest du Volleyball spielen? Mach mit!',
                'button_label_ne': 'सदस्यता लिनुहोस्',
                'button_label_en': 'Get Membership',
                'button_label_de': 'Mitglied werden',
                'button_link': '/membership'
            }
        )

        self.stdout.write(self.style.SUCCESS('Team Page content updated'))

        # 05. Membership Page
        membership_page, _ = MembershipPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'सदस्यता - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Membership - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Mitgliedschaft - Nepal Volleyball Club Hamburg e.V.',
                'meta_description_ne': 'हाम्रो समुदायमा सामेल हुनुहोस् र हामीलाई बढ्न मद्दत गर्नुहोस्।',
                'meta_description_en': 'Join our community and help us grow.',
                'meta_description_de': 'Treten Sie unserer Gemeinschaft bei und helfen Sie uns zu wachsen.',
            }
        )

        MembershipHero.objects.update_or_create(
            page=membership_page,
            defaults={
                'title_ne': 'सदस्यता',
                'title_en': 'Membership',
                'title_de': 'Mitgliedschaft',
                'text_ne': 'नेपाल भलिबल क्लब हामबर्ग e.V. को परिवारमा सामेल हुनुहोस् र भलिबल खेल्दै समुदायको विकासमा योगदान दिनुहोस्।',
                'text_en': 'Join the Nepal Volleyball Club Hamburg e.V. family and contribute to community development while playing volleyball.',
                'text_de': 'Werde Teil der Familie des Nepal Volleyball Club Hamburg e.V. und trage durch Volleyball zur Entwicklung der Gemeinschaft bei.',
                'image_url': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=1600&q=80'
            }
        )

        benefits_data = [
            {
                'title_ne': 'टोलीको हिस्सा', 'title_en': 'Part of a Team', 'title_de': 'TEIL EINES TEAMS',
                'desc_ne': 'हाम्रो क्लबको सदस्य बनेर एक जीवन्त भलिबल समुदायको हिस्सा बन्नुहोस्।',
                'desc_en': 'Become part of a vibrant volleyball community by joining our club.',
                'desc_de': 'Werden Sie Teil einer lebendigen Volleyball-Gemeinschaft, indem Sie unserem Verein beitreten.',
                'icon': 'Users'
            },
            {
                'title_ne': 'नियमित प्रशिक्षण', 'title_en': 'Regular Training', 'title_de': 'REGELMÄSSIGES TRAINING',
                'desc_ne': 'अनुभवी प्रशिक्षकहरूको नेतृत्वमा नियमित प्रशिक्षण सत्रहरूमा सहभागी हुनुहोस्।',
                'desc_en': 'Participate in regular training sessions led by experienced coaches.',
                'desc_de': 'Nehmen Sie an regelmäßigen Trainingseinheiten unter der Leitung erfahrener Trainer teil.',
                'icon': 'Award'
            },
            {
                'title_ne': 'क्लब कार्यक्रमहरू', 'title_en': 'Club Events', 'title_de': 'CLUB EVENTS',
                'desc_ne': 'क्लबद्वारा आयोजित विशेष कार्यक्रमहरू र प्रतियोगिताहरूमा भाग लिनुहोस्।',
                'desc_en': 'Join exclusive events and tournaments organized by the club.',
                'desc_de': 'Nehmen Sie an exklusiven Veranstaltungen und Turnieren teil, die vom Club organisiert werden.',
                'icon': 'Heart'
            }
        ]

        MembershipBenefit.objects.filter(page=membership_page).delete()
        for i, benefit in enumerate(benefits_data):
            MembershipBenefit.objects.create(
                page=membership_page,
                order=i,
                **benefit
            )

        MembershipFormSettings.objects.update_or_create(
            page=membership_page,
            defaults={
                'title_ne': 'सदस्यता फारम',
                'title_en': 'Membership Form',
                'title_de': 'Mitgliedschaftsformular',
                'text_ne': 'तलको फारम भर्नुहोस्। हामी तपाईंलाई छिट्टै सम्पर्क गर्नेछौं।',
                'text_en': 'Fill out the form below. We will contact you shortly.',
                'text_de': 'Füllen Sie das untenstehende Formular aus. Wir werden uns bald bei Ihnen melden.',
                'success_title_ne': 'धन्यवाद!',
                'success_title_en': 'Thank You!',
                'success_title_de': 'Vielen Dank!',
                'success_text_ne': 'तपाईंको सदस्यता आवेदन प्राप्त भयो। हामी छिट्टै सम्पर्क गर्नेछौं।',
                'success_text_en': 'We received your membership application. We will contact you shortly.',
                'success_text_de': 'Wir haben Ihren Mitgliedsantrag erhalten. Wir werden uns in Kürze bei Ihnen melden.',
                # Labels & Options are defaulted in model, but can be customized here if needed
            }
        )

        self.stdout.write(self.style.SUCCESS('Membership Page content updated'))

        # 06. Events Page
        events_page, _ = EventsPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'कार्यक्रमहरू - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Events - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Veranstaltungen - Nepal Volleyball Club Hamburg e.V.',
            }
        )

        EventsHero.objects.update_or_create(
            page=events_page,
            defaults={
                'title_ne': 'कार्यक्रमहरू',
                'title_en': 'Events',
                'title_de': 'Veranstaltungen',
                'text_ne': 'आगामी र विगतका भलिबल प्रतियोगिता तथा सामुदायिक कार्यक्रमहरूको जानकारी।',
                'text_en': 'Information on upcoming and past volleyball tournaments and community events.',
                'text_de': 'Informationen zu kommenden und vergangenen Volleyballturnieren und Gemeinschaftsveranstaltungen.',
                'image_url': 'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=1600&q=80'
            }
        )

        EventsSettings.objects.update_or_create(
            page=events_page,
            defaults={
                'upcoming_title_ne': 'आगामी कार्यक्रमहरू',
                'upcoming_title_en': 'Upcoming Events',
                'upcoming_title_de': 'Kommende Veranstaltungen',
                'past_title_ne': 'विगतका कार्यक्रमहरू',
                'past_title_en': 'Past Events',
                'past_title_de': 'Vergangene Veranstaltungen',
                'register_btn_ne': 'दर्ता गर्नुहोस्',
                'register_btn_en': 'Register',
                'register_btn_de': 'Registrieren',
                'label_upcoming_ne': 'आगामी',
                'label_upcoming_en': 'Upcoming',
                'label_upcoming_de': 'Kommende',
                'label_past_ne': 'विगत',
                'label_past_en': 'Past',
                'label_past_de': 'Vergangene',
            }
        )

        upcoming_data = [
            {
                'title_ne': 'वसन्त भलिबल प्रतियोगिता २०२६', 'title_en': 'Spring Volleyball Tournament 2026', 'title_de': 'Frühlings-Volleyballturnier 2026',
                'date_text_ne': 'मार्च १५, २०२६', 'date_text_en': 'March 15, 2026', 'date_text_de': '15. März 2026',
                'time': '10:00 AM', 'location_ne': 'Hamburg Sports Hall', 'location_en': 'Hamburg Sports Hall', 'location_de': 'Sporthalle Hamburg',
                'description_ne': 'हामबर्गमा आयोजना हुने वार्षिक भलिबल प्रतियोगिता। विभिन्न क्लबहरूको सहभागिता।',
                'description_en': 'Annual volleyball tournament held in Hamburg. Participation of various clubs.',
                'description_de': 'Jährliches Volleyballturnier in Hamburg. Teilnahme verschiedener Vereine.',
                'image_url': 'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=600&q=80',
                'is_past': False
            },
            {
                'title_ne': 'नेपाली नयाँ वर्ष महोत्सव', 'title_en': 'Nepali New Year Festival', 'title_de': 'Nepalesisches Neujahrsfest',
                'date_text_ne': 'अप्रिल ५, २०२६', 'date_text_en': 'April 5, 2026', 'date_text_de': '5. April 2026',
                'time': '2:00 PM', 'location_ne': 'Community Center Hamburg', 'location_en': 'Community Center Hamburg', 'location_de': 'Bürgerhaus Hamburg',
                'description_ne': 'नयाँ वर्ष २०८३ को अवसरमा सांस्कृतिक कार्यक्रम र भलिबल प्रदर्शनी।',
                'description_en': 'Cultural program and volleyball exhibition on the occasion of New Year 2083.',
                'description_de': 'Kulturprogramm und Volleyball-Ausstellung anlässlich des neuen Jahres 2083.',
                'image_url': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=600&q=80',
                'is_past': False
            },
            {
                'title_ne': 'ग्रीष्मकालीन प्रशिक्षण शिविर', 'title_en': 'Summer Training Camp', 'title_de': 'Sommer-Trainingslager',
                'date_text_ne': 'जुन १-७, २०२६', 'date_text_en': 'June 1-7, 2026', 'date_text_de': '1.-7. Juni 2026',
                'time': '9:00 AM', 'location_ne': 'Sports Academy Hamburg', 'location_en': 'Sports Academy Hamburg', 'location_de': 'Sportakademie Hamburg',
                'description_ne': 'एक हप्ताको गहन भलिबल प्रशिक्षण कार्यक्रम। सबै स्तरका खेलाडीहरूको लागि।',
                'description_en': 'One week intensive volleyball training program. For players of all levels.',
                'description_de': 'Einwöchiges intensives Volleyball-Trainingsprogramm. Für Spieler aller Niveaus.',
                'image_url': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=600&q=80',
                'is_past': False
            }
        ]

        past_data = [
            {
                'title_ne': 'शीतकालीन भलिबल लिग २०२५', 'title_en': 'Winter Volleyball League 2025', 'title_de': 'Winter-Volleyballliga 2025',
                'date_text_ne': 'डिसेम्बर १५, २०२५', 'date_text_en': 'December 15, 2025', 'date_text_de': '15. Dezember 2025',
                'location_ne': 'Hamburg Indoor Stadium', 'location_en': 'Hamburg Indoor Stadium', 'location_de': 'Hallenstadion Hamburg',
                'image_url': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?w=600&q=80',
                'is_past': True
            },
            {
                'title_ne': 'दशैं तिहार भेला २०२५', 'title_en': 'Dashain Tihar Gathering 2025', 'title_de': 'Dashain Tihar Treffen 2025',
                'date_text_ne': 'अक्टोबर २०, २०२५', 'date_text_en': 'October 20, 2025', 'date_text_de': '20. Oktober 2025',
                'location_ne': 'Community Hall', 'location_en': 'Community Hall', 'location_de': 'Gemeindehalle',
                'image_url': 'https://images.unsplash.com/photo-1551958219-acbc608c6377?w=600&q=80',
                'is_past': True
            }
        ]

        Event.objects.filter(page=events_page).delete()
        for i, event in enumerate(upcoming_data + past_data):
            Event.objects.create(
                page=events_page,
                order=i,
                **event
            )

        self.stdout.write(self.style.SUCCESS('Events Page content updated'))

        # 07. News Page
        news_page, _ = NewsPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'समाचार - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'News - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Neuigkeiten - Nepal Volleyball Club Hamburg e.V.',
            }
        )

        NewsHero.objects.update_or_create(
            page=news_page,
            defaults={
                'title_ne': 'समाचार',
                'title_en': 'News',
                'title_de': 'Neuigkeiten',
                'text_ne': 'क्लबको नवीनतम समाचार, उपलब्धि र गतिविधिहरूको जानकारी।',
                'text_en': 'Information on the club\'s latest news, achievements and activities.',
                'text_de': 'Informationen zu den neuesten Nachrichten, Erfolgen und Aktivitäten des Vereins.',
                'image_url': 'https://images.unsplash.com/photo-1504450758481-7338eba7524a?w=1600&q=80'
            }
        )

        NewsSettings.objects.update_or_create(
            page=news_page,
            defaults={
                'featured_label_ne': 'मुख्य समाचार',
                'featured_label_en': 'Featured News',
                'featured_label_de': 'Top-Nachricht',
                'read_more_label_ne': 'पूरा पढ्नुहोस्',
                'read_more_label_en': 'Read More',
                'read_more_label_de': 'Weiterlesen',
                'other_news_title_ne': 'अन्य समाचार',
                'other_news_title_en': 'Other News',
                'other_news_title_de': 'Weitere Neuigkeiten',
            }
        )

        categories_data = [
            {'ne': 'साझेदारी', 'en': 'Partnership', 'de': 'Partnerschaft'},
            {'ne': 'प्रशिक्षण', 'en': 'Training', 'de': 'Training'},
            {'ne': 'प्रतियोगिता', 'en': 'Tournament', 'de': 'Wettbewerb'},
            {'ne': 'सदस्यता', 'en': 'Membership', 'de': 'Mitgliedschaft'},
        ]

        category_objs = {}
        for i, cat in enumerate(categories_data):
            obj, _ = NewsCategory.objects.update_or_create(
                name_en=cat['en'],
                defaults={
                    'name_ne': cat['ne'],
                    'name_de': cat['de'],
                    'order': i
                }
            )
            category_objs[cat['en']] = obj

        articles_data = [
            {
                'title_ne': 'क्लबले जर्मन भलिबल संघसँग साझेदारी गर्यो', 'title_en': 'Club Partners with German Volleyball Association', 'title_de': 'Verein kooperiert mit Deutschem Volleyball-Verband',
                'excerpt_ne': 'नेपाल भलिबल क्लब हामबर्ग e.V. ले जर्मन भलिबल संघसँग आधिकारिक साझेदारी गरेको छ। यो साझेदारीले...',
                'excerpt_en': 'Nepal Volleyball Club Hamburg e.V. has officially partnered with the German Volleyball Association. This partnership...',
                'excerpt_de': 'Nepal Volleyball Club Hamburg e.V. ist offiziell eine Partnerschaft mit dem Deutschen Volleyball-Verband eingegangen. Diese Partnerschaft...',
                'date_text_ne': 'फेब्रुअरी २५, २०२६', 'date_text_en': 'February 25, 2026', 'date_text_de': '25. Februar 2026',
                'category_key': 'Partnership',
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1577223625816-7546f13df25d?w=600&q=80'
            },
            {
                'title_ne': 'नयाँ प्रशिक्षण कार्यक्रम सुरु', 'title_en': 'New Training Program Started', 'title_de': 'Neues Trainingsprogramm gestartet',
                'excerpt_ne': 'क्लबले नयाँ खेलाडीहरूको लागि विशेष प्रशिक्षण कार्यक्रम सुरु गरेको छ। यो कार्यक्रममा...',
                'excerpt_en': 'The club has started a special training program for new players. In this program...',
                'excerpt_de': 'Der Verein hat ein spezielles Trainingsprogramm für neue Spieler gestartet. In diesem Programm...',
                'date_text_ne': 'फेब्रुअरी २०, २०२६', 'date_text_en': 'February 20, 2026', 'date_text_de': '20. Februar 2026',
                'category_key': 'Training',
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=600&q=80'
            },
            {
                'title_ne': 'शीतकालीन प्रतियोगितामा तेस्रो स्थान', 'title_en': 'Third Place in Winter Tournament', 'title_de': 'Dritter Platz beim Winterturnier',
                'excerpt_ne': 'हाम्रो टोलीले हामबर्ग शीतकालीन भलिबल प्रतियोगितामा तेस्रो स्थान हासिल गर्न सफल भयो।',
                'excerpt_en': 'Our team successfully secured third place in the Hamburg Winter Volleyball Tournament.',
                'excerpt_de': 'Unser Team hat erfolgreich den dritten Platz beim Hamburger Winter-Volleyballturnier belegt.',
                'date_text_ne': 'डिसेम्बर १८, २०२५', 'date_text_en': 'December 18, 2025', 'date_text_de': '18. Dezember 2025',
                'category_key': 'Tournament',
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?w=600&q=80'
            },
            {
                'title_ne': '५० जना नयाँ सदस्य थपिए', 'title_en': '50 New Members Added', 'title_de': '50 neue Mitglieder hinzugefügt',
                'excerpt_ne': '२०२५ मा क्लबमा ५० जना नयाँ सदस्य थपिएका छन्। यसले हाम्रो समुदाय बढ्दै गएको देखाउँछ।',
                'excerpt_en': '50 new members have been added to the club in 2025. This shows our community is growing.',
                'excerpt_de': 'Im Jahr 2025 sind 50 neue Mitglieder zum Verein hinzugekommen. Dies zeigt, dass unsere Gemeinschaft wächst.',
                'date_text_ne': 'डिसेम्बर १०, २०२५', 'date_text_en': 'December 10, 2025', 'date_text_de': '10. Dezember 2025',
                'category_key': 'Membership',
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1551958219-acbc608c6377?w=600&q=80'
            }
        ]

        NewsArticle.objects.filter(page=news_page).delete()
        for i, art in enumerate(articles_data):
            cat_key = art.pop('category_key')
            NewsArticle.objects.create(
                page=news_page,
                order=i,
                category=category_objs.get(cat_key),
                **art
            )

        self.stdout.write(self.style.SUCCESS('News Page content updated'))

        # 08. Gallery Page
        gallery_page, _ = GalleryPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'ग्यालरी - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Gallery - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Galerie - Nepal Volleyball Club Hamburg e.V.',
            }
        )

        GalleryHero.objects.update_or_create(
            page=gallery_page,
            defaults={
                'title_ne': 'ग्यालरी',
                'title_en': 'Gallery',
                'title_de': 'Galerie',
                'text_ne': 'क्लबका विभिन्न कार्यक्रम, प्रतियोगिता र सामुदायिक गतिविधिका तस्बिरहरू।',
                'text_en': 'Photos of various club events, tournaments and community activities.',
                'text_de': 'Fotos von verschiedenen Vereinsveranstaltungen, Turnieren und Gemeinschaftsaktivitäten.',
            }
        )

        gallery_categories = [
            {'ne': 'सबै', 'en': 'All', 'de': 'Alle'},
            {'ne': 'प्रतियोगिता', 'en': 'Tournament', 'de': 'Turnier'},
            {'ne': 'प्रशिक्षण', 'en': 'Training', 'de': 'Training'},
            {'ne': 'सामुदायिक', 'en': 'Community', 'de': 'Gemeinschaft'},
            {'ne': 'उत्सव', 'en': 'Festival', 'de': 'Festival'},
        ]

        gallery_cat_objs = {}
        for i, cat in enumerate(gallery_categories):
            obj, _ = GalleryCategory.objects.update_or_create(
                name_en=cat['en'],
                defaults={'name_ne': cat['ne'], 'name_de': cat['de'], 'order': i}
            )
            gallery_cat_objs[cat['en']] = obj

        gallery_images = [
            {'cat': 'Tournament', 'title_ne': 'वसन्त प्रतियोगिता २०२५', 'title_en': 'Spring Tournament 2025', 'title_de': 'Frühlingsturnier 2025', 'url': 'https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800&q=80'},
            {'cat': 'Training', 'title_ne': 'साप्ताहिक प्रशिक्षण', 'title_en': 'Weekly Training', 'title_de': 'Wöchentliches Training', 'url': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800&q=80'},
            {'cat': 'Tournament', 'title_ne': 'शीतकालीन लिग', 'title_en': 'Winter League', 'title_de': 'Winterliga', 'url': 'https://images.unsplash.com/photo-1612872087720-bb876e2e67d1?w=800&q=80'},
            {'cat': 'Community', 'title_ne': 'सामुदायिक भेला', 'title_en': 'Community Gathering', 'title_de': 'Gemeinschaftstreffen', 'url': 'https://images.unsplash.com/photo-1551958219-acbc608c6377?w=800&q=80'},
            {'cat': 'Festival', 'title_ne': 'दशैं भेला', 'title_en': 'Dashain Gathering', 'title_de': 'Dashain Treffen', 'url': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800&q=80'},
        ]

        GalleryImage.objects.filter(page=gallery_page).delete()
        for i, img in enumerate(gallery_images):
            GalleryImage.objects.create(
                page=gallery_page,
                category=gallery_cat_objs.get(img['cat']),
                image_url=img['url'],
                title_ne=img['title_ne'],
                title_en=img['title_en'],
                title_de=img['title_de'],
                order=i
            )

        GallerySettings.objects.update_or_create(
            page=gallery_page,
            defaults={
                'no_images_text_ne': 'यो श्रेणीमा कुनै तस्बिर छैन।',
                'no_images_text_en': 'No photos in this category.',
                'no_images_text_de': 'Keine Fotos in dieser Kategorie.',
            }
        )

        self.stdout.write(self.style.SUCCESS('Gallery Page content updated'))

        # 09. Contact Page
        contact_page, _ = ContactPage.objects.update_or_create(
            id=1,
            defaults={
                'status': 'published',
                'meta_title_ne': 'सम्पर्क - नेपाल भलिबल क्लब हामबर्ग e.V.',
                'meta_title_en': 'Contact - Nepal Volleyball Club Hamburg e.V.',
                'meta_title_de': 'Kontakt - Nepal Volleyball Club Hamburg e.V.',
            }
        )

        ContactHero.objects.update_or_create(
            page=contact_page,
            defaults={
                'title_ne': 'सम्पर्क',
                'title_en': 'Contact Us',
                'title_de': 'Kontaktieren Sie uns',
                'subtitle_ne': 'हामीसँग सम्पर्क गर्नुहोस्',
                'subtitle_en': 'Get in touch with us',
                'subtitle_de': 'Kontaktieren Sie uns',
                'image_url': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1600&q=80'
            }
        )

        contact_methods = [
            {'icon': 'MapPin', 'label_ne': 'ठेगाना', 'label_en': 'Address', 'label_de': 'Adresse', 'value': 'Hellkamp 30, 20255 Hamburg, Germany'},
            {'icon': 'Phone', 'label_ne': 'फोन', 'label_en': 'Phone', 'label_de': 'Telefon', 'value': '+49 160 8176707'},
            {'icon': 'Mail', 'label_ne': 'इमेल', 'label_en': 'Email', 'label_de': 'E-Mail', 'value': 'nvchdeutschland@gmail.com'},
        ]

        ContactInfo.objects.filter(page=contact_page).delete()
        for i, method in enumerate(contact_methods):
            ContactInfo.objects.create(page=contact_page, order=i, **method)

        social_links = [
            {'platform': 'Facebook', 'icon': 'Facebook', 'url': 'https://facebook.com/volleyballnepal'},
            {'platform': 'Instagram', 'icon': 'Instagram', 'url': 'https://instagram.com/volleyballnepal'},
            {'platform': 'Twitter', 'icon': 'Twitter', 'url': 'https://twitter.com/volleyballnepal'},
        ]

        ContactSocial.objects.filter(page=contact_page).delete()
        for i, link in enumerate(social_links):
            ContactSocial.objects.create(page=contact_page, order=i, **link)

        ContactSettings.objects.update_or_create(
            page=contact_page,
            defaults={
                'form_title_ne': 'सन्देश पठाउनुहोस्',
                'form_title_en': 'Send Message',
                'form_title_de': 'Nachricht senden',
                'info_section_title_ne': 'सम्पर्क जानकारी',
                'info_section_title_en': 'Contact Information',
                'info_section_title_de': 'Kontaktinformationen',
                'social_section_title_ne': 'सामाजिक सञ्जाल',
                'social_section_title_en': 'Social Media',
                'social_section_title_de': 'Soziale Medien',
            }
        )

        self.stdout.write(self.style.SUCCESS('Contact Page content updated'))
