import os
import json
from datetime import datetime
import re


def get_hardcoded_bug_log(site_id):
    """Get hardcoded bug log for a specific site"""

    # Hardcoded bug logs for all sites
    bug_logs = {
        1: {
            "template_name":
            "drinking-water-website-template",
            "site_id":
            1,
            "total_bugs":
            30,
            "html_bugs":
            15,
            "css_bugs":
            15,
            "bugs": [{
                "id": "HTML-001",
                "type": "missing_doctype",
                "difficulty": "easy",
                "original": "<!DOCTYPE html>",
                "modified": "",
                "description": "Removed DOCTYPE declaration"
            }, {
                "id": "HTML-002",
                "type": "invalid_tag",
                "difficulty": "medium",
                "original": "<body>",
                "modified": "<bod>",
                "description": "Changed body to bod"
            }, {
                "id": "HTML-003",
                "type": "missing_closing_tag",
                "difficulty": "easy",
                "original": "</div>\n    <!-- Spinner End -->",
                "modified": "\n    <!-- Spinner End -->",
                "description": "Missing closing div in spinner"
            }, {
                "id": "HTML-004",
                "type": "attribute_typo",
                "difficulty": "easy",
                "original": "class=\"navbar-nav",
                "modified": "clas=\"navbar-nav",
                "description": "Typo in class attribute"
            }, {
                "id": "HTML-005",
                "type": "missing_quotes",
                "difficulty": "easy",
                "original": "class=\"btn btn-primary\"",
                "modified": "class=btn btn-primary",
                "description": "Missing quotes in class attribute"
            }, {
                "id": "HTML-006",
                "type": "tag_typo",
                "difficulty": "easy",
                "original": "<div class=\"container\">",
                "modified": "<dvi class=\"container\">",
                "description": "Changed div to dvi"
            }, {
                "id": "HTML-007",
                "type": "missing_alt",
                "difficulty": "easy",
                "original": "alt=\"\"",
                "modified": "",
                "description": "Removed alt attribute"
            }, {
                "id": "HTML-008",
                "type": "broken_href",
                "difficulty": "easy",
                "original": "href=\"#about\"",
                "modified": "href=\"#abou\"",
                "description": "Broken href link"
            }, {
                "id": "HTML-009",
                "type": "extra_space",
                "difficulty": "medium",
                "original": "<div class=\"row\">",
                "modified": "< div class=\"row\">",
                "description": "Extra space in div tag"
            }, {
                "id": "HTML-010",
                "type": "missing_bracket",
                "difficulty": "medium",
                "original": "<div class=\"col-lg-6\">",
                "modified": "<div class=\"col-lg-6\"",
                "description": "Missing closing bracket"
            }, {
                "id": "HTML-011",
                "type": "nested_mismatch",
                "difficulty": "medium",
                "original": "<h1>Clean Water</h1>",
                "modified": "<h1>Clean Water</div>",
                "description": "Mismatched nested tags"
            }, {
                "id": "HTML-012",
                "type": "missing_meta",
                "difficulty": "medium",
                "original":
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
                "modified": "",
                "description": "Removed viewport meta tag"
            }, {
                "id": "HTML-013",
                "type": "broken_comment",
                "difficulty": "hard",
                "original": "<!-- Spinner Start -->",
                "modified": "<!- Spinner Start -->",
                "description": "Broken HTML comment"
            }, {
                "id": "HTML-014",
                "type": "invisible_char",
                "difficulty": "hard",
                "original": "Read More",
                "modified": "Read\u200BMore",
                "description": "Invisible character injection"
            }, {
                "id": "HTML-015",
                "type": "self_closing",
                "difficulty": "hard",
                "original": "<br>",
                "modified": "<br />",
                "description": "Self-closing tag formatting"
            }, {
                "id": "CSS-016",
                "type": "missing_semicolon",
                "difficulty": "easy",
                "original": "opacity: 0;",
                "modified": "opacity: 0",
                "description": "Missing semicolon in opacity"
            }, {
                "id": "CSS-017",
                "type": "missing_brace",
                "difficulty": "medium",
                "original": "z-index: 99999;\n}",
                "modified": "z-index: 99999;\n",
                "description": "Missing closing brace"
            }, {
                "id": "CSS-018",
                "type": "property_typo",
                "difficulty": "easy",
                "original": "background:",
                "modified": "backgrund:",
                "description": "Typo in background property"
            }, {
                "id": "CSS-019",
                "type": "invalid_unit",
                "difficulty": "easy",
                "original": "30px",
                "modified": "30pix",
                "description": "Invalid CSS unit"
            }, {
                "id": "CSS-020",
                "type": "missing_bracket",
                "difficulty": "easy",
                "original": ".btn-square {",
                "modified": ".btn-square ",
                "description": "Missing CSS bracket"
            }, {
                "id": "CSS-021",
                "type": "invalid_variable",
                "difficulty": "medium",
                "original": "var(--bs-white)",
                "modified": "var(--bs-whiteG)",
                "description": "Invalid CSS variable name"
            }, {
                "id": "CSS-022",
                "type": "missing_colon",
                "difficulty": "easy",
                "original": "color:",
                "modified": "color ",
                "description": "Missing colon in color property"
            }, {
                "id": "CSS-023",
                "type": "invalid_selector",
                "difficulty": "medium",
                "original": ".navbar-brand",
                "modified": ".navbar-brand$",
                "description": "Invalid CSS selector character"
            }, {
                "id": "CSS-024",
                "type": "media_query_typo",
                "difficulty": "medium",
                "original": "@media (max-width: 991.98px)",
                "modified": "@mdia (max-width: 991.98px)",
                "description": "Typo in media query"
            }, {
                "id": "CSS-025",
                "type": "flexbox_typo",
                "difficulty": "medium",
                "original": "justify-content:",
                "modified": "justify-conten:",
                "description": "Typo in flexbox property"
            }, {
                "id": "CSS-026",
                "type": "pseudo_class_typo",
                "difficulty": "medium",
                "original": ":hover",
                "modified": ":hove",
                "description": "Typo in hover pseudo-class"
            }, {
                "id": "CSS-027",
                "type": "variable_syntax",
                "difficulty": "hard",
                "original": "var(--bs-primary)",
                "modified": "var(-bs-primary)",
                "description": "CSS variable syntax error"
            }, {
                "id": "CSS-028",
                "type": "transform_typo",
                "difficulty": "hard",
                "original": "transform:",
                "modified": "transfor:",
                "description": "Typo in transform property"
            }, {
                "id": "CSS-029",
                "type": "important_typo",
                "difficulty": "hard",
                "original": "!important",
                "modified": "!importan",
                "description": "Typo in !important declaration"
            }, {
                "id": "CSS-030",
                "type": "invalid_percentage",
                "difficulty": "hard",
                "original": "100%",
                "modified": "100percent",
                "description": "Invalid percentage unit"
            }]
        },
        2: {
            "template_name":
            "mobile-app-html-template",
            "site_id":
            2,
            "total_bugs":
            30,
            "html_bugs":
            15,
            "css_bugs":
            15,
            "bugs": [{
                "id": "HTML-001",
                "type": "missing_doctype",
                "difficulty": "easy",
                "original": "<!DOCTYPE html>",
                "modified": "",
                "description": "Removed DOCTYPE declaration"
            }, {
                "id": "HTML-002",
                "type": "invalid_tag",
                "difficulty": "medium",
                "original": "<body>",
                "modified": "<bod>",
                "description": "Changed body to bod"
            }, {
                "id": "HTML-003",
                "type": "missing_closing_tag",
                "difficulty": "easy",
                "original": "</div>\n    <!-- Contact Us -->",
                "modified": "\n    <!-- Contact Us -->",
                "description": "Missing closing div in contact section"
            }, {
                "id": "HTML-004",
                "type": "attribute_typo",
                "difficulty": "easy",
                "original": "class=\"navbar-nav",
                "modified": "clas=\"navbar-nav",
                "description": "Typo in class attribute"
            }, {
                "id": "HTML-005",
                "type": "missing_quotes",
                "difficulty": "easy",
                "original": "class=\"btn btn-primary\"",
                "modified": "class=btn btn-primary",
                "description": "Missing quotes in class attribute"
            }, {
                "id": "HTML-006",
                "type": "tag_typo",
                "difficulty": "easy",
                "original": "<div class=\"container\">",
                "modified": "<dvi class=\"container\">",
                "description": "Changed div to dvi"
            }, {
                "id": "HTML-007",
                "type": "missing_alt",
                "difficulty": "easy",
                "original": "alt=\"\"",
                "modified": "",
                "description": "Removed alt attribute"
            }, {
                "id": "HTML-008",
                "type": "broken_href",
                "difficulty": "easy",
                "original": "href=\"#\"",
                "modified": "href=\"#broken\"",
                "description": "Broken href link"
            }, {
                "id": "HTML-009",
                "type": "extra_space",
                "difficulty": "medium",
                "original": "<div class=\"row\">",
                "modified": "< div class=\"row\">",
                "description": "Extra space in div tag"
            }, {
                "id": "HTML-010",
                "type": "missing_bracket",
                "difficulty": "medium",
                "original": "<div class=\"col-lg-6\">",
                "modified": "<div class=\"col-lg-6\"",
                "description": "Missing closing bracket"
            }, {
                "id": "HTML-011",
                "type": "nested_mismatch",
                "difficulty": "medium",
                "original": "<h1>Read More</h1>",
                "modified": "<h1>Read More</div>",
                "description": "Mismatched nested tags"
            }, {
                "id": "HTML-012",
                "type": "missing_meta",
                "difficulty": "medium",
                "original":
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
                "modified": "",
                "description": "Removed viewport meta tag"
            }, {
                "id": "HTML-013",
                "type": "broken_comment",
                "difficulty": "hard",
                "original": "<!-- Contact Us -->",
                "modified": "<!- Contact Us -->",
                "description": "Broken HTML comment"
            }, {
                "id": "HTML-014",
                "type": "invisible_char",
                "difficulty": "hard",
                "original": "Contact Us",
                "modified": "Contact\u200BUs",
                "description": "Invisible character injection"
            }, {
                "id": "HTML-015",
                "type": "self_closing",
                "difficulty": "hard",
                "original": "<br>",
                "modified": "<br />",
                "description": "Self-closing tag formatting"
            }, {
                "id": "CSS-016",
                "type": "missing_semicolon",
                "difficulty": "easy",
                "original": "opacity: 0;",
                "modified": "opacity: 0",
                "description": "Missing semicolon in opacity"
            }, {
                "id": "CSS-017",
                "type": "missing_brace",
                "difficulty": "medium",
                "original": "z-index: 99999;\n}",
                "modified": "z-index: 99999;\n",
                "description": "Missing closing brace"
            }, {
                "id": "CSS-018",
                "type": "property_typo",
                "difficulty": "easy",
                "original": "background:",
                "modified": "backgrund:",
                "description": "Typo in background property"
            }, {
                "id": "CSS-019",
                "type": "invalid_unit",
                "difficulty": "easy",
                "original": "38px",
                "modified": "38pix",
                "description": "Invalid CSS unit"
            }, {
                "id": "CSS-020",
                "type": "missing_bracket",
                "difficulty": "easy",
                "original": ".btn-square {",
                "modified": ".btn-square ",
                "description": "Missing CSS bracket"
            }, {
                "id": "CSS-021",
                "type": "invalid_variable",
                "difficulty": "medium",
                "original": "var(--primary)",
                "modified": "var(--primaryX)",
                "description": "Invalid CSS variable name"
            }, {
                "id": "CSS-022",
                "type": "missing_colon",
                "difficulty": "easy",
                "original": "color:",
                "modified": "color ",
                "description": "Missing colon in color property"
            }, {
                "id": "CSS-023",
                "type": "invalid_selector",
                "difficulty": "medium",
                "original": ".navbar-light",
                "modified": ".navbar-light$",
                "description": "Invalid CSS selector character"
            }, {
                "id": "CSS-024",
                "type": "media_query_typo",
                "difficulty": "medium",
                "original": "@media (max-width: 991.98px)",
                "modified": "@mdia (max-width: 991.98px)",
                "description": "Typo in media query"
            }, {
                "id": "CSS-025",
                "type": "flexbox_typo",
                "difficulty": "medium",
                "original": "justify-content:",
                "modified": "justify-conten:",
                "description": "Typo in flexbox property"
            }, {
                "id": "CSS-026",
                "type": "pseudo_class_typo",
                "difficulty": "medium",
                "original": ":hover",
                "modified": ":hove",
                "description": "Typo in hover pseudo-class"
            }, {
                "id": "CSS-027",
                "type": "variable_syntax",
                "difficulty": "hard",
                "original": "var(--secondary)",
                "modified": "var(-secondary)",
                "description": "CSS variable syntax error"
            }, {
                "id": "CSS-028",
                "type": "transform_typo",
                "difficulty": "hard",
                "original": "transform:",
                "modified": "transfor:",
                "description": "Typo in transform property"
            }, {
                "id": "CSS-029",
                "type": "important_typo",
                "difficulty": "hard",
                "original": "!important",
                "modified": "!importan",
                "description": "Typo in !important declaration"
            }, {
                "id": "CSS-030",
                "type": "invalid_percentage",
                "difficulty": "hard",
                "original": "100%",
                "modified": "100percent",
                "description": "Invalid percentage unit"
            }]
        },
        3: {
            "template_name":
            "online-shop-website-template",
            "site_id":
            3,
            "total_bugs":
            30,
            "html_bugs":
            15,
            "css_bugs":
            15,
            "bugs": [{
                "id": "HTML-001",
                "type": "missing_doctype",
                "difficulty": "easy",
                "original": "<!DOCTYPE html>",
                "modified": "",
                "description": "Removed DOCTYPE declaration"
            }, {
                "id": "HTML-002",
                "type": "invalid_tag",
                "difficulty": "medium",
                "original": "<body>",
                "modified": "<bod>",
                "description": "Changed body to bod"
            }, {
                "id": "HTML-003",
                "type": "missing_closing_tag",
                "difficulty": "easy",
                "original": "</div>\n    <!-- Shop End -->",
                "modified": "\n    <!-- Shop End -->",
                "description": "Missing closing div in shop section"
            }, {
                "id": "HTML-004",
                "type": "attribute_typo",
                "difficulty": "easy",
                "original": "class=\"navbar-nav",
                "modified": "clas=\"navbar-nav",
                "description": "Typo in class attribute"
            }, {
                "id": "HTML-005",
                "type": "missing_quotes",
                "difficulty": "easy",
                "original": "class=\"btn btn-primary\"",
                "modified": "class=btn btn-primary",
                "description": "Missing quotes in class attribute"
            }, {
                "id": "HTML-006",
                "type": "tag_typo",
                "difficulty": "easy",
                "original": "<div class=\"container-fluid\">",
                "modified": "<dvi class=\"container-fluid\">",
                "description": "Changed div to dvi"
            }, {
                "id": "HTML-007",
                "type": "missing_alt",
                "difficulty": "easy",
                "original": "alt=\"\"",
                "modified": "",
                "description": "Removed alt attribute"
            }, {
                "id": "HTML-008",
                "type": "broken_href",
                "difficulty": "easy",
                "original": "href=\"shop.html\"",
                "modified": "href=\"sho.html\"",
                "description": "Broken shop.html link"
            }, {
                "id": "HTML-009",
                "type": "extra_space",
                "difficulty": "medium",
                "original": "<div class=\"row\">",
                "modified": "< div class=\"row\">",
                "description": "Extra space in div tag"
            }, {
                "id": "HTML-010",
                "type": "missing_bracket",
                "difficulty": "medium",
                "original": "<div class=\"col-lg-4\">",
                "modified": "<div class=\"col-lg-4\"",
                "description": "Missing closing bracket"
            }, {
                "id": "HTML-011",
                "type": "nested_mismatch",
                "difficulty": "medium",
                "original": "<h3>Shop Now</h3>",
                "modified": "<h3>Shop Now</div>",
                "description": "Mismatched nested tags"
            }, {
                "id": "HTML-012",
                "type": "missing_meta",
                "difficulty": "medium",
                "original":
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
                "modified": "",
                "description": "Removed viewport meta tag"
            }, {
                "id": "HTML-013",
                "type": "broken_comment",
                "difficulty": "hard",
                "original": "<!-- Shop Start -->",
                "modified": "<!- Shop Start -->",
                "description": "Broken HTML comment"
            }, {
                "id": "HTML-014",
                "type": "invisible_char",
                "difficulty": "hard",
                "original": "Add To Cart",
                "modified": "Add\u200BTo Cart",
                "description": "Invisible character in 'Add To Cart'"
            }, {
                "id": "HTML-015",
                "type": "self_closing",
                "difficulty": "hard",
                "original": "<img",
                "modified": "<img /",
                "description": "Improper img tag formatting"
            }, {
                "id": "CSS-016",
                "type": "missing_semicolon",
                "difficulty": "easy",
                "original": "opacity: 0;",
                "modified": "opacity: 0",
                "description": "Missing semicolon in opacity"
            }, {
                "id": "CSS-017",
                "type": "missing_brace",
                "difficulty": "medium",
                "original": "z-index: 99999;\n}",
                "modified": "z-index: 99999;\n",
                "description": "Missing closing brace"
            }, {
                "id": "CSS-018",
                "type": "property_typo",
                "difficulty": "easy",
                "original": "background:",
                "modified": "backgrund:",
                "description": "Typo in background property"
            }, {
                "id": "CSS-019",
                "type": "invalid_unit",
                "difficulty": "easy",
                "original": "25px",
                "modified": "25pix",
                "description": "Invalid CSS unit"
            }, {
                "id": "CSS-020",
                "type": "missing_bracket",
                "difficulty": "easy",
                "original": ".btn-outline {",
                "modified": ".btn-outline ",
                "description": "Missing CSS bracket"
            }, {
                "id": "CSS-021",
                "type": "invalid_variable",
                "difficulty": "medium",
                "original": "var(--bs-primary)",
                "modified": "var(--bs-primaryX)",
                "description": "Invalid CSS variable name"
            }, {
                "id": "CSS-022",
                "type": "missing_colon",
                "difficulty": "easy",
                "original": "color:",
                "modified": "color ",
                "description": "Missing colon in color property"
            }, {
                "id": "CSS-023",
                "type": "invalid_selector",
                "difficulty": "medium",
                "original": ".product-item",
                "modified": ".product-item$",
                "description": "Invalid product-item selector"
            }, {
                "id": "CSS-024",
                "type": "media_query_typo",
                "difficulty": "medium",
                "original": "@media (max-width: 991.98px)",
                "modified": "@mdia (max-width: 991.98px)",
                "description": "Typo in media query"
            }, {
                "id": "CSS-025",
                "type": "flexbox_typo",
                "difficulty": "medium",
                "original": "align-items:",
                "modified": "align-item:",
                "description": "Typo in align-items property"
            }, {
                "id": "CSS-026",
                "type": "pseudo_class_typo",
                "difficulty": "medium",
                "original": ":hover",
                "modified": ":hove",
                "description": "Typo in hover pseudo-class"
            }, {
                "id": "CSS-027",
                "type": "variable_syntax",
                "difficulty": "hard",
                "original": "var(--bs-secondary)",
                "modified": "var(-bs-secondary)",
                "description": "CSS variable syntax error"
            }, {
                "id": "CSS-028",
                "type": "transform_typo",
                "difficulty": "hard",
                "original": "translateY",
                "modified": "translateX",
                "description": "Wrong transform function"
            }, {
                "id": "CSS-029",
                "type": "important_typo",
                "difficulty": "hard",
                "original": "!important",
                "modified": "!importan",
                "description": "Typo in !important declaration"
            }, {
                "id": "CSS-030",
                "type": "invalid_percentage",
                "difficulty": "hard",
                "original": "100%",
                "modified": "100percent",
                "description": "Invalid percentage unit"
            }]
        },
        4: {
            "template_name":
            "seo-agency-website-template",
            "site_id":
            4,
            "total_bugs":
            30,
            "html_bugs":
            15,
            "css_bugs":
            15,
            "bugs": [{
                "id": "HTML-001",
                "type": "missing_doctype",
                "difficulty": "easy",
                "original": "<!DOCTYPE html>",
                "modified": "",
                "description": "Removed DOCTYPE declaration"
            }, {
                "id": "HTML-002",
                "type": "invalid_tag",
                "difficulty": "medium",
                "original": "<body>",
                "modified": "<bod>",
                "description": "Changed body to bod"
            }, {
                "id": "HTML-003",
                "type": "missing_closing_tag",
                "difficulty": "easy",
                "original": "</div>\n    <!-- Service End -->",
                "modified": "\n    <!-- Service End -->",
                "description": "Missing closing div in service section"
            }, {
                "id": "HTML-004",
                "type": "attribute_typo",
                "difficulty": "easy",
                "original": "class=\"navbar-nav",
                "modified": "clas=\"navbar-nav",
                "description": "Typo in class attribute"
            }, {
                "id": "HTML-005",
                "type": "missing_quotes",
                "difficulty": "easy",
                "original": "class=\"btn btn-primary\"",
                "modified": "class=btn btn-primary",
                "description": "Missing quotes in class attribute"
            }, {
                "id": "HTML-006",
                "type": "tag_typo",
                "difficulty": "easy",
                "original": "<div class=\"container\">",
                "modified": "<dvi class=\"container\">",
                "description": "Changed div to dvi"
            }, {
                "id": "HTML-007",
                "type": "missing_alt",
                "difficulty": "easy",
                "original": "alt=\"\"",
                "modified": "",
                "description": "Removed alt attribute"
            }, {
                "id": "HTML-008",
                "type": "broken_href",
                "difficulty": "easy",
                "original": "href=\"#service\"",
                "modified": "href=\"#servic\"",
                "description": "Broken service link"
            }, {
                "id": "HTML-009",
                "type": "extra_space",
                "difficulty": "medium",
                "original": "<div class=\"row\">",
                "modified": "< div class=\"row\">",
                "description": "Extra space in div tag"
            }, {
                "id": "HTML-010",
                "type": "missing_bracket",
                "difficulty": "medium",
                "original": "<div class=\"col-lg-6\">",
                "modified": "<div class=\"col-lg-6\"",
                "description": "Missing closing bracket"
            }, {
                "id": "HTML-011",
                "type": "nested_mismatch",
                "difficulty": "medium",
                "original": "<h2>SEO Services</h2>",
                "modified": "<h2>SEO Services</div>",
                "description": "Mismatched nested tags"
            }, {
                "id": "HTML-012",
                "type": "missing_meta",
                "difficulty": "medium",
                "original":
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
                "modified": "",
                "description": "Removed viewport meta tag"
            }, {
                "id": "HTML-013",
                "type": "broken_comment",
                "difficulty": "hard",
                "original": "<!-- Service Start -->",
                "modified": "<!- Service Start -->",
                "description": "Broken HTML comment"
            }, {
                "id": "HTML-014",
                "type": "invisible_char",
                "difficulty": "hard",
                "original": "Read More",
                "modified": "Read\u200BMore",
                "description": "Invisible character injection"
            }, {
                "id": "HTML-015",
                "type": "self_closing",
                "difficulty": "hard",
                "original": "<br>",
                "modified": "<br />",
                "description": "Self-closing tag formatting"
            }, {
                "id": "CSS-016",
                "type": "missing_semicolon",
                "difficulty": "easy",
                "original": "opacity: 0;",
                "modified": "opacity: 0",
                "description": "Missing semicolon in opacity"
            }, {
                "id": "CSS-017",
                "type": "missing_brace",
                "difficulty": "medium",
                "original": "z-index: 99999;\n}",
                "modified": "z-index: 99999;\n",
                "description": "Missing closing brace"
            }, {
                "id": "CSS-018",
                "type": "property_typo",
                "difficulty": "easy",
                "original": "background:",
                "modified": "backgrund:",
                "description": "Typo in background property"
            }, {
                "id": "CSS-019",
                "type": "invalid_unit",
                "difficulty": "easy",
                "original": "38px",
                "modified": "38pix",
                "description": "Invalid CSS unit"
            }, {
                "id": "CSS-020",
                "type": "missing_bracket",
                "difficulty": "easy",
                "original": ".btn-square {",
                "modified": ".btn-square ",
                "description": "Missing CSS bracket"
            }, {
                "id": "CSS-021",
                "type": "invalid_variable",
                "difficulty": "medium",
                "original": "var(--primary)",
                "modified": "var(--primaryX)",
                "description": "Invalid CSS variable name"
            }, {
                "id": "CSS-022",
                "type": "missing_colon",
                "difficulty": "easy",
                "original": "color:",
                "modified": "color ",
                "description": "Missing colon in color property"
            }, {
                "id": "CSS-023",
                "type": "invalid_selector",
                "difficulty": "medium",
                "original": ".service-item",
                "modified": ".service-item$",
                "description": "Invalid service-item selector"
            }, {
                "id": "CSS-024",
                "type": "media_query_typo",
                "difficulty": "medium",
                "original": "@media (max-width: 991.98px)",
                "modified": "@mdia (max-width: 991.98px)",
                "description": "Typo in media query"
            }, {
                "id": "CSS-025",
                "type": "flexbox_typo",
                "difficulty": "medium",
                "original": "justify-content:",
                "modified": "justify-conten:",
                "description": "Typo in flexbox property"
            }, {
                "id": "CSS-026",
                "type": "pseudo_class_typo",
                "difficulty": "medium",
                "original": ":hover",
                "modified": ":hove",
                "description": "Typo in hover pseudo-class"
            }, {
                "id": "CSS-027",
                "type": "variable_syntax",
                "difficulty": "hard",
                "original": "var(--secondary)",
                "modified": "var(-secondary)",
                "description": "CSS variable syntax error"
            }, {
                "id": "CSS-028",
                "type": "transition_typo",
                "difficulty": "hard",
                "original": "transition:",
                "modified": "transitio:",
                "description": "Typo in transition property"
            }, {
                "id": "CSS-029",
                "type": "important_typo",
                "difficulty": "hard",
                "original": "!important",
                "modified": "!importan",
                "description": "Typo in !important declaration"
            }, {
                "id": "CSS-030",
                "type": "invalid_percentage",
                "difficulty": "hard",
                "original": "100%",
                "modified": "100percent",
                "description": "Invalid percentage unit"
            }]
        },
        5: {
            "template_name":
            "stock-market-website-template",
            "site_id":
            5,
            "total_bugs":
            30,
            "html_bugs":
            15,
            "css_bugs":
            15,
            "bugs": [{
                "id": "HTML-001",
                "type": "missing_doctype",
                "difficulty": "easy",
                "original": "<!DOCTYPE html>",
                "modified": "",
                "description": "Removed DOCTYPE declaration"
            }, {
                "id": "HTML-002",
                "type": "invalid_tag",
                "difficulty": "medium",
                "original": "<body>",
                "modified": "<bod>",
                "description": "Changed body to bod"
            }, {
                "id":
                "HTML-003",
                "type":
                "missing_closing_tag",
                "difficulty":
                "easy",
                "original":
                "</div>\n    <!-- Testimonial End -->",
                "modified":
                "\n    <!-- Testimonial End -->",
                "description":
                "Missing closing div in testimonial section"
            }, {
                "id": "HTML-004",
                "type": "attribute_typo",
                "difficulty": "easy",
                "original": "class=\"navbar-nav",
                "modified": "clas=\"navbar-nav",
                "description": "Typo in class attribute"
            }, {
                "id": "HTML-005",
                "type": "missing_quotes",
                "difficulty": "easy",
                "original": "class=\"btn btn-primary\"",
                "modified": "class=btn btn-primary",
                "description": "Missing quotes in class attribute"
            }, {
                "id": "HTML-006",
                "type": "tag_typo",
                "difficulty": "easy",
                "original": "<div class=\"container\">",
                "modified": "<dvi class=\"container\">",
                "description": "Changed div to dvi"
            }, {
                "id": "HTML-007",
                "type": "missing_alt",
                "difficulty": "easy",
                "original": "alt=\"\"",
                "modified": "",
                "description": "Removed alt attribute"
            }, {
                "id": "HTML-008",
                "type": "broken_href",
                "difficulty": "easy",
                "original": "href=\"#team\"",
                "modified": "href=\"#tea\"",
                "description": "Broken team link"
            }, {
                "id": "HTML-009",
                "type": "extra_space",
                "difficulty": "medium",
                "original": "<div class=\"row\">",
                "modified": "< div class=\"row\">",
                "description": "Extra space in div tag"
            }, {
                "id": "HTML-010",
                "type": "missing_bracket",
                "difficulty": "medium",
                "original": "<div class=\"col-lg-6\">",
                "modified": "<div class=\"col-lg-6\"",
                "description": "Missing closing bracket"
            }, {
                "id": "HTML-011",
                "type": "nested_mismatch",
                "difficulty": "medium",
                "original": "<h4>Profession</h4>",
                "modified": "<h4>Profession</div>",
                "description": "Mismatched nested tags"
            }, {
                "id": "HTML-012",
                "type": "missing_meta",
                "difficulty": "medium",
                "original":
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
                "modified": "",
                "description": "Removed viewport meta tag"
            }, {
                "id": "HTML-013",
                "type": "broken_comment",
                "difficulty": "hard",
                "original": "<!-- Team Start -->",
                "modified": "<!- Team Start -->",
                "description": "Broken HTML comment"
            }, {
                "id": "HTML-014",
                "type": "invisible_char",
                "difficulty": "hard",
                "original": "Learn More",
                "modified": "Learn\u200BMore",
                "description": "Invisible character in Learn More"
            }, {
                "id": "HTML-015",
                "type": "self_closing",
                "difficulty": "hard",
                "original": "<br>",
                "modified": "<br />",
                "description": "Self-closing tag formatting"
            }, {
                "id": "CSS-016",
                "type": "missing_semicolon",
                "difficulty": "easy",
                "original": "opacity: 0;",
                "modified": "opacity: 0",
                "description": "Missing semicolon in opacity"
            }, {
                "id": "CSS-017",
                "type": "missing_brace",
                "difficulty": "medium",
                "original": "z-index: 99999;\n}",
                "modified": "z-index: 99999;\n",
                "description": "Missing closing brace"
            }, {
                "id": "CSS-018",
                "type": "property_typo",
                "difficulty": "easy",
                "original": "background:",
                "modified": "backgrund:",
                "description": "Typo in background property"
            }, {
                "id": "CSS-019",
                "type": "invalid_unit",
                "difficulty": "easy",
                "original": "32px",
                "modified": "32pix",
                "description": "Invalid CSS unit"
            }, {
                "id": "CSS-020",
                "type": "missing_bracket",
                "difficulty": "easy",
                "original": ".btn-square {",
                "modified": ".btn-square ",
                "description": "Missing CSS bracket"
            }, {
                "id": "CSS-021",
                "type": "invalid_variable",
                "difficulty": "medium",
                "original": "var(--bs-white)",
                "modified": "var(--bs-whiteX)",
                "description": "Invalid CSS variable name"
            }, {
                "id": "CSS-022",
                "type": "missing_colon",
                "difficulty": "easy",
                "original": "color:",
                "modified": "color ",
                "description": "Missing colon in color property"
            }, {
                "id": "CSS-023",
                "type": "invalid_selector",
                "difficulty": "medium",
                "original": ".team-item",
                "modified": ".team-item$",
                "description": "Invalid team-item selector"
            }, {
                "id": "CSS-024",
                "type": "media_query_typo",
                "difficulty": "medium",
                "original": "@media (max-width: 991.98px)",
                "modified": "@mdia (max-width: 991.98px)",
                "description": "Typo in media query"
            }, {
                "id": "CSS-025",
                "type": "flexbox_typo",
                "difficulty": "medium",
                "original": "justify-content:",
                "modified": "justify-conten:",
                "description": "Typo in flexbox property"
            }, {
                "id": "CSS-026",
                "type": "pseudo_class_typo",
                "difficulty": "medium",
                "original": ":hover",
                "modified": ":hove",
                "description": "Typo in hover pseudo-class"
            }, {
                "id": "CSS-027",
                "type": "variable_syntax",
                "difficulty": "hard",
                "original": "var(--bs-primary)",
                "modified": "var(-bs-primary)",
                "description": "CSS variable syntax error"
            }, {
                "id": "CSS-028",
                "type": "transform_typo",
                "difficulty": "hard",
                "original": "transform:",
                "modified": "transfor:",
                "description": "Typo in transform property"
            }, {
                "id": "CSS-029",
                "type": "important_typo",
                "difficulty": "hard",
                "original": "!important",
                "modified": "!importan",
                "description": "Typo in !important declaration"
            }, {
                "id": "CSS-030",
                "type": "invalid_percentage",
                "difficulty": "hard",
                "original": "100%",
                "modified": "100percent",
                "description": "Invalid percentage unit"
            }]
        }
    }

    return bug_logs.get(site_id)


def load_bug_log(site_id):
    """Load bug log for a specific site - now uses hardcoded data"""
    return get_hardcoded_bug_log(site_id)


def verify_specific_bugs(content, bug_list):
    """Verify specific bugs are fixed in the content"""
    score = 0
    fixed_bugs = 0

    for bug in bug_list:
        bug_type = bug.get("type", "")
        original = bug.get("original", "")
        modified = bug.get("modified", "")
        difficulty = bug.get("difficulty", "easy")

        # Scoring based on difficulty
        points = {"easy": 10, "medium": 20, "hard": 30}.get(difficulty, 10)

        is_fixed = False

        # Check different bug types
        if bug_type == "missing_doctype":
            is_fixed = "<!DOCTYPE html>" in content

        elif bug_type == "invalid_tag":
            if "body" in original and "bod" in modified:
                is_fixed = "<body>" in content and "<bod>" not in content

        elif bug_type == "attribute_typo":
            if "class=" in original and "clas=" in modified:
                is_fixed = content.count("class=") > content.count("clas=")

        elif bug_type == "missing_quotes":
            if 'class="' in original and 'class=' in modified:
                quoted = len(re.findall(r'class="[^"]*"', content))
                unquoted = len(re.findall(r'class=[^"\s>]+', content))
                is_fixed = quoted > unquoted

        elif bug_type == "missing_semicolon":
            if original.endswith(";") and not modified.endswith(";"):
                is_fixed = original in content

        elif bug_type == "property_typo":
            if ":" in original and ":" in modified:
                correct_prop = original.split(":")[0]
                wrong_prop = modified.split(":")[0]
                is_fixed = correct_prop in content and wrong_prop not in content

        # Generic check: if modified (buggy) code is gone and original is present
        elif modified and original:
            is_fixed = (modified not in content) and (original in content)

        elif original:
            is_fixed = original in content

        if is_fixed:
            score += points
            fixed_bugs += 1

    return score, fixed_bugs


def check_all_fixes(folder, expected_site_id):
    """Enhanced check fixes with real bug verification using hardcoded logs"""
    score = 0

    # Convert expected_site_id to int if it's a string
    try:
        expected_site_id = int(expected_site_id)
    except (ValueError, TypeError):
        return 0

    # Load site configuration (keep existing validation)
    try:
        sites_path = os.path.join('admin', 'sites.json')
        if not os.path.exists(sites_path):
            print(f"Warning: sites.json not found at {sites_path}")
        else:
            with open(sites_path, 'r') as f:
                sites = json.load(f)

            if str(expected_site_id) not in sites:
                print(f"Invalid site ID: {expected_site_id}")
                return 0
    except Exception as e:
        print(f"Error loading sites config: {e}")

    # Check if folder exists
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return 0

    # Load hardcoded bug log
    bug_data = load_bug_log(expected_site_id)

    if bug_data:
        # Real bug verification using hardcoded data
        print(f"Using hardcoded bug verification for site {expected_site_id}")

        # Read HTML and CSS files
        html_content = ""
        css_content = ""

        html_file = os.path.join(folder, "index.html")
        css_file = os.path.join(folder, "css", "style.css")

        try:
            if os.path.exists(html_file):
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
        except Exception as e:
            print(f"Error reading HTML: {e}")

        try:
            if os.path.exists(css_file):
                with open(css_file, 'r', encoding='utf-8') as f:
                    css_content = f.read()
        except Exception as e:
            print(f"Error reading CSS: {e}")

        # Verify HTML bugs
        html_bugs = [
            bug for bug in bug_data.get("bugs", [])
            if bug.get("id", "").startswith("HTML")
        ]
        css_bugs = [
            bug for bug in bug_data.get("bugs", [])
            if bug.get("id", "").startswith("CSS")
        ]

        html_score, html_fixed = verify_specific_bugs(html_content, html_bugs)
        css_score, css_fixed = verify_specific_bugs(css_content, css_bugs)

        total_score = html_score + css_score
        total_fixed = html_fixed + css_fixed
        total_bugs = len(bug_data.get("bugs", []))

        print(f"Site ID: {expected_site_id}")
        print(
            f"HTML bugs fixed: {html_fixed}/{len(html_bugs)} (Score: {html_score})"
        )
        print(
            f"CSS bugs fixed: {css_fixed}/{len(css_bugs)} (Score: {css_score})"
        )
        print(f"Total bugs fixed: {total_fixed}/{total_bugs}")
        print(f"Total score: {total_score}")

        return total_score

    else:
        # Fallback to original file-based scoring
        print(f"Using fallback scoring for site {expected_site_id}")

        # Updated for your actual template structure
        site_files = {
            1: ['index.html', 'css/style.css'],
            2: ['index.html', 'css/style.css'],
            3: ['index.html', 'css/style.css'],
            4: ['index.html', 'css/style.css'],
            5: ['index.html', 'css/style.css'],
        }

        required_files = site_files.get(expected_site_id,
                                        ['index.html', 'css/style.css'])

        # Score based on presence of required files
        found_files = []
        missing_files = []

        for file in required_files:
            file_path = os.path.join(folder, file)
            if os.path.exists(file_path):
                found_files.append(file)
                if file.endswith('.html'):
                    score += 200  # Base score for HTML presence
                elif file.endswith('.css'):
                    score += 100  # Base score for CSS presence
            else:
                missing_files.append(file)

        print(f"Site ID: {expected_site_id}")
        print(f"Required files: {required_files}")
        print(f"Found files: {found_files}")
        print(f"Missing files: {missing_files}")
        print(f"Total score: {score}")

        return score


# Keep all your existing functions unchanged
def update_leaderboard(participant_name,
                       site_id,
                       score,
                       leaderboard_file='leaderboard.json'):
    """Update the leaderboard with participant's score"""
    # Load existing leaderboard or create new one
    leaderboard = []
    if os.path.exists(leaderboard_file):
        try:
            with open(leaderboard_file, 'r') as f:
                leaderboard = json.load(f)
        except Exception as e:
            print(f"Error loading leaderboard: {e}")
            leaderboard = []

    # Create entry for this submission
    entry = {
        'participant': participant_name,
        'site_id': site_id,
        'score': score,
        'timestamp': datetime.now().isoformat(),
        'max_possible': 900  # Updated max possible score (30 bugs * 30 points)
    }

    # Find if participant already exists for this site
    participant_exists = False
    for i, existing_entry in enumerate(leaderboard):
        if (existing_entry['participant'] == participant_name
                and existing_entry['site_id'] == site_id):
            # Update if new score is better
            if score > existing_entry['score']:
                leaderboard[i] = entry
                print(
                    f"Updated {participant_name}'s score for site {site_id}: {score}"
                )
            else:
                print(
                    f"Score not improved for {participant_name} on site {site_id}"
                )
            participant_exists = True
            break

    # Add new entry if participant doesn't exist for this site
    if not participant_exists:
        leaderboard.append(entry)
        print(
            f"Added new entry for {participant_name} on site {site_id}: {score}"
        )

    # Sort leaderboard by score (descending)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    # Save updated leaderboard
    try:
        with open(leaderboard_file, 'w') as f:
            json.dump(leaderboard, f, indent=2)
        print(f"Leaderboard updated successfully")
    except Exception as e:
        print(f"Error saving leaderboard: {e}")

    return leaderboard


def display_leaderboard(leaderboard_file='leaderboard.json', top_n=10):
    """Display the current leaderboard"""
    if not os.path.exists(leaderboard_file):
        print("No leaderboard found")
        return

    try:
        with open(leaderboard_file, 'r') as f:
            leaderboard = json.load(f)
    except Exception as e:
        print(f"Error loading leaderboard: {e}")
        return

    if not leaderboard:
        print("Leaderboard is empty")
        return

    print(f"\n{'='*60}")
    print(f"{'LEADERBOARD - TOP ' + str(top_n):^60}")
    print(f"{'='*60}")
    print(
        f"{'Rank':<6} {'Participant':<20} {'Site':<6} {'Score':<8} {'Time':<15}"
    )
    print(f"{'-'*60}")

    for i, entry in enumerate(leaderboard[:top_n]):
        rank = i + 1
        participant = entry['participant'][:18]
        site_id = entry['site_id']
        score = entry['score']
        timestamp = entry['timestamp'][:16]

        print(
            f"{rank:<6} {participant:<20} {site_id:<6} {score:<8} {timestamp:<15}"
        )

    print(f"{'='*60}\n")


def run_test(participant_name, folder_path, expected_site_id):
    """Run a complete test for a participant"""
    print(f"\nTesting submission for {participant_name}")
    print(f"Folder: {folder_path}")
    print(f"Expected Site ID: {expected_site_id}")
    print("-" * 50)

    # Check the fixes
    score = check_all_fixes(folder_path, expected_site_id)

    # Update leaderboard
    leaderboard = update_leaderboard(participant_name, expected_site_id, score)

    # Display current leaderboard
    display_leaderboard()

    return score


def get_detailed_results(folder_path, site_id):
    """Get detailed bug checking results using hardcoded logs"""
    bug_data = load_bug_log(site_id)

    if not bug_data:
        return {
            "score": 0,
            "total_bugs": 0,
            "fixed_bugs": 0,
            "details": [],
            "percentage": 0
        }

    # Read files
    html_content = ""
    css_content = ""

    html_file = os.path.join(folder_path, "index.html")
    css_file = os.path.join(folder_path, "css", "style.css")

    try:
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
    except Exception as e:
        print(f"Error reading files: {e}")

    # Check bugs
    total_score = 0
    fixed_count = 0
    details = []

    for bug in bug_data.get("bugs", []):
        content_to_check = html_content if bug.get(
            "id", "").startswith("HTML") else css_content
        score, fixed = verify_specific_bugs(content_to_check, [bug])

        if fixed > 0:
            fixed_count += 1
            total_score += score

        details.append({
            "id": bug.get("id"),
            "description": bug.get("description"),
            "difficulty": bug.get("difficulty"),
            "status": "✅ Fixed" if fixed > 0 else "❌ Not Fixed",
            "score": score
        })

    total_bugs = len(bug_data.get("bugs", []))

    return {
        "score":
        total_score,
        "total_bugs":
        total_bugs,
        "fixed_bugs":
        fixed_count,
        "details":
        details,
        "percentage":
        round((fixed_count / total_bugs) * 100, 1) if total_bugs > 0 else 0
    }


# Example usage
if __name__ == "__main__":
    # Test with sample data
    test_cases = [
        ("Alice", "submissions/alice", 1),
        ("Bob", "submissions/bob", 2),
        ("Charlie", "submissions/charlie", 3),
    ]

    for participant, folder, site_id in test_cases:
        score = run_test(participant, folder, site_id)
        print(f"Final score for {participant}: {score}\n")
