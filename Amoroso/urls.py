from django.conf.urls import include, url

from views import add_todo

from views import gast_anmeldung
from views import gutschein_einloesen
from views import link_to_detail_sites
from views import delete_empty_cart_message
from views import profil_bearbeiten
from views import profil_aktualisieren
from views import passwort_bearbeiten
from views import passwort_aktualisieren
from views import adressbuch_bearbeiten
from views import VIP_bearbeiten
from views import ueber_uns_2
from views import adresse_speichern
from views import zahlungsmethoden_bearbeiten
from views import zahlungsmethode_speichern
from views import bestellungen_ansehen
from views import bestellungen_details_ansehen
from views import bewertungen_bearbeiten
from views import bewertung_abgeben
from views import bewertung_speichern
from views import bestellung_zuruecksenden
from views import save_preliminary_quiz_results
from views import passform_quiz

from views import gutscheinkonto
from views import log_out
from views import facebook_login

from views import freunde_einladen

from views import bestellen

from views import bestellen_pre_test
from views import warenkorb_aufrufen
from views import login_user
from views import register_user
from views import updater_user_registration
from views import load_account_page
from views import kollektion_abrufen

from views import bestellung_abrufen

from views import bestelldetails_abrufen

from views import check_mobilnummer

from views import warenkorb_abrufen

from views import generate_lingerie

from views import content_abrufen
from views import filter_abrufen
from views import new_value_for_wishlist
from views import ruecksendung_beauftragen
from views import sendungsverfolgung_tracken
from views import groessentabelle_uebersicht
from views import groessentabelle_detailliert

from views import quiz_beenden
from views import quiz_abrufen
from views import start_page_real
from views import full_text_search
from views import decipher_marketing_email_click

from views import big_data_farbe_click
from views import big_data_picture_clicked
from views import big_data_cart_put
from views import big_data_wishlist_put
from views import big_data_initial_input_detailed_page
from views import big_data_initial_input_main_page
from views import newsletter_abmelden_page

from views import big_data_color_click_main_page
from views import big_data_picture_click_main_page
from views import big_data_wishlist_click_main_page
from views import big_data_filter_click_main_page
from views import skip_VIP

from views import get_gutschein_value

from views import get_money_back_VIP
from views import select_shopping_type
from views import get_rebates
from views import check_log_in
from views import verschicke_gutscheine
from views import verschicke_gutscheine_send_email
from views import referral_message_shown

from views import impressum

from views import credit_card_test

from views import test_creditcard

from views import zahlungsmethode_speichern_test

from views import payment_credit_card_test

from views import paypal_test

from views import paypal_verficiation
from views import ueber_uns
from views import datenschutz
from views import widerrufsbelehrung
from views import agb
from views import support

from views import sofortueberweisung_not_successful

from views import sofortueberweisung_successful

from views import get_link_based_on_lingerie_name
from views import ruecksendung_calcualte_wert
from views import test_email

from views import passwort_aendern_passwort_vergessen

from views import request_passwort_vergessen

from views import passwort_vergessen_page

from views import passwort_vergessen_bestaetigen
from views import get_cart_from_server

from views import bestellung_versenden

from views import versandettikett_drucken
from views import get_sendungsverfolgung

from views import rueckversand_erhalten

from views import rueckerstattung_veranlassen
from views import ruecksendungen_abrufen

from views import cart_data_sent_to_google_analytics

from views import send_email_support
from views import VIP_mitgliedschaft_kuendigen

from views import cancel_VIP
from views import cart_aufrufen

from views import zur_kasse

from views import laenderinteresse
from views import test_rechnung
from views import get_rabattname_from_request
from views import pursue_VIP_payments
from views import email_adresse_zu_bestaetigen
from views import anmeldung_bestaetigen
from views import onleave_message_abrufen
from views import get_adressbuch_daten
from views import band_cup_recommendation

from views import versand_rueckversand

from views import wishlist_abrufen

from views import newsletter_abmelden

from views import dhl_fill_out_form
from views import sofortueberweisung_status
from views import wie_funktioniert_VIP
from django.conf.urls import url, include

from views import email_marketing
from views import quiz_fitting
from views import submit_quiz_results
from views import kein_quiz

urlpatterns = [
    url(r'^test_rechnung/$', test_rechnung),
    url(r'^dhl_fill_out_form/$', dhl_fill_out_form),
    url(r'^paypal_verficiation/$', paypal_verficiation),
    url(r'^paypal_test/$', paypal_test),
    url(r'^test_email/$', test_email),
    url(r'^payment_credit_card_test/$', payment_credit_card_test),
    url(r'^get_sendungsverfolgung/$', get_sendungsverfolgung),
    url(r'^cart_data_sent_to_google_analytics/$', cart_data_sent_to_google_analytics),

    url(r'^band_cup_recommendation/$', band_cup_recommendation),

    url(r'^checkout/sofortueberweisung_status/([^/]+)/$', sofortueberweisung_status),

    url(r'^save_preliminary_quiz_results/$', save_preliminary_quiz_results),
    url(r'^get_cart_from_server/$', get_cart_from_server),

    url(r'^gast_anmeldung/$', gast_anmeldung),
    url(r'^login_user/$', login_user),
    url(r'^register_user/$', register_user),
    url(r'^updater_user_registration/$', updater_user_registration),
    url(r'^$', start_page_real),

    url(r'^test_creditcard/$', test_creditcard),
    url(r'^get_link_based_on_lingerie_name/$', get_link_based_on_lingerie_name),
    url(r'^account_page/passwort_aendern_passwort_vergessen/$', passwort_aendern_passwort_vergessen),
    url(r'^account_page/request_passwort_vergessen/$', request_passwort_vergessen),

    url(r'^passwort_vergessen/$', passwort_vergessen_page),
    url(r'^passwort_vergessen_bestaetigen/([^/]+)/$', passwort_vergessen_bestaetigen),

    url(r'^send_email_support/$', send_email_support),

    url(r'^get_rabattname_from_request/$', get_rabattname_from_request),
    url(r'^email_adresse_zu_bestaetigen/$', email_adresse_zu_bestaetigen),

    url(r'^anmeldung_bestaetigen/([^/]+)/$', anmeldung_bestaetigen),
    url(r'^onleave_message_abrufen/$', onleave_message_abrufen),
    url(r'^get_adressbuch_daten/$', get_adressbuch_daten),
    url(r'^email_marketing/([^/]+)/$', email_marketing),

    url(r'^passform_quiz/$', passform_quiz),

    url(r'^cart/$', cart_aufrufen),
    url(r'^checkout/$', warenkorb_aufrufen),
    url(r'^checkout/sofortueberweisung_not_successful/([^/]+)/$', sofortueberweisung_not_successful),

    url(r'^checkout/sofortueberweisung_successful/([^/]+)/$', sofortueberweisung_successful),

    url(r'^account_page/zahlungsmethode_speichern_test/$', zahlungsmethode_speichern_test),
    url(r'^account_page/cancel_VIP/$', cancel_VIP),

    url(r'^Produktauswahl/([^/]+)/([^/]+)/$', link_to_detail_sites),
    url(r'^add/$', add_todo),
    url(r'^bestellen/$', bestellen),
    url(r'^ruecksendung_calcualte_wert/$', ruecksendung_calcualte_wert),

    url(r'^bestellen_pre_test/$', bestellen_pre_test),
    url(r'^zur_kasse/$', zur_kasse),

    url(r'^submit_quiz_results/$', submit_quiz_results),

    url(r'^gutschein_einloesen/$', gutschein_einloesen),
    url(r'^account_page/$', load_account_page),
    url(r'^account_page/profil_bearbeiten/$', profil_bearbeiten),
    url(r'^account_page/profil_aktualisieren/$', profil_aktualisieren),
    url(r'^account_page/passwort_bearbeiten/$', passwort_bearbeiten),
    url(r'^account_page/passwort_aktualisieren/$', passwort_aktualisieren),
    url(r'^account_page/adressbuch_bearbeiten/$', adressbuch_bearbeiten),
    url(r'^account_page/VIP_bearbeiten/$', VIP_bearbeiten),
    url(r'^account_page/VIP_bearbeiten/VIP_kuendigung/$', VIP_mitgliedschaft_kuendigen),

    url(r'^quiz_fitting/$', quiz_fitting),

    url(r'^account_page/adresse_speichern/$', adresse_speichern),
    url(r'^account_page/zahlungsmethoden_bearbeiten/$', zahlungsmethoden_bearbeiten),
    url(r'^account_page/zahlungsmethode_speichern/$', zahlungsmethode_speichern),
    url(r'^account_page/bestellungen_ansehen/$', bestellungen_ansehen),
    url(r'^account_page/bestellungen_ansehen/([^/]+)/$', bestellungen_details_ansehen),
    url(r'^account_page/sendungsverfolgung_tracken/([^/]+)/$', sendungsverfolgung_tracken),
    url(r'^account_page/bewertungen_bearbeiten/([^/]+)/$', bewertungen_bearbeiten),
    url(r'^account_page/bewertung_speichern/$', bewertung_speichern),
    url(r'^account_page/bestellung_zuruecksenden/$', bestellung_zuruecksenden),

    url(r'^versand_rueckversand/$', versand_rueckversand),
    url(r'^account_page/gutscheinkonto/$', gutscheinkonto),
    url(r'^log_out/$', log_out),
    url(r'^facebook_login/$', facebook_login),
    url(r'^account_page/freunde_einladen/$', verschicke_gutscheine),
    url(r'^einladung/$', freunde_einladen),
    url(r'^referral_message_shown/$', referral_message_shown),
    url(r'^delete_empty_cart_message/$', delete_empty_cart_message),

    url(r'^message_click/$', decipher_marketing_email_click),
    url(r'^kein_quiz/$', kein_quiz),

    url(r'^wishlist_abrufen/$', wishlist_abrufen),

    url(r'^kollektion_abrufen/$', kollektion_abrufen),

    url(r'^bestellung_abrufen/$', bestellung_abrufen),

    url(r'^bestelldetails_abrufen/$', bestelldetails_abrufen),

    url(r'^check_mobilnummer/$', check_mobilnummer),
    url(r'^warenkorb_abrufen/$', warenkorb_abrufen),
    url(r'^full_text_search/$', full_text_search),

    url(r'^Produktauswahl/([^/]+)/$', generate_lingerie),

    url(r'^content_abrufen/$', content_abrufen),
    url(r'^filter_abrufen/$', filter_abrufen),

    url(r'^new_value_for_wishlist/$', new_value_for_wishlist),
    url(r'^account_page/groessentabelle_uebersicht/$', groessentabelle_uebersicht),
    url(r'^account_page/groessentabelle_detailliert/$', groessentabelle_detailliert),

    url(r'^quiz_beenden/$', quiz_beenden),
    url(r'^quiz_abrufen/$', quiz_abrufen),

    url(r'^account_page/ruecksendung_beauftragen/$', ruecksendung_beauftragen),

    url(r'^big_data_farbe_click/$', big_data_farbe_click),
    url(r'^big_data_picture_clicked/$', big_data_picture_clicked),
    url(r'^big_data_cart_put/$', big_data_cart_put),
    url(r'^big_data_wishlist_put/$', big_data_wishlist_put),
    url(r'^big_data_initial_input_detailed_page/$', big_data_initial_input_detailed_page),

    url(r'^big_data_initial_input_main_page/$', big_data_initial_input_main_page),

    url(r'^big_data_color_click_main_page/$', big_data_color_click_main_page),

    url(r'^big_data_picture_click_main_page/$', big_data_picture_click_main_page),

    url(r'^big_data_wishlist_click_main_page/$', big_data_wishlist_click_main_page),

    url(r'^get_gutschein_value/$', get_gutschein_value),
    url(r'^skip_VIP/$', skip_VIP),

    url(r'^get_money_back_VIP/$', get_money_back_VIP),

    url(r'^account_page/bewertungen_bearbeiten/([^/]+)/([^/]+)/$', bewertung_abgeben),
    url(r'^newsletter_abmelden/$', newsletter_abmelden),

    url(r'^newsletter_abmelden_page/$', newsletter_abmelden_page),

    url(r'^big_data_filter_click_main_page/$', big_data_filter_click_main_page),

    url(r'^select_shopping_type/$', select_shopping_type),

    url(r'^get_rebates/$', get_rebates),
    url(r'^check_log_in/$', check_log_in),
    url(r'^verschicke_gutscheine_send_email/$', verschicke_gutscheine_send_email),
    url(r'^ruecksendungen_abrufen/$', ruecksendungen_abrufen),

    url(r'^wie_funktioniert_VIP/$', wie_funktioniert_VIP),

    url(r'^ueber_uns_2/$', ueber_uns_2),
    url(r'^impressum/$', impressum),
    url(r'^ueber_uns/$', ueber_uns),
    url(r'^datenschutz/$', datenschutz),
    url(r'^widerrufsbelehrung/$', widerrufsbelehrung),
    url(r'^agb/$', agb),
    url(r'^support/$', support),

    url(r'^laenderinteresse/$', laenderinteresse)

]

