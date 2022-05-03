from os import environ


SESSION_CONFIGS = [
    dict(
        name='all_in_one',
        display_name="All in one",
        app_sequence=['introduction',
                      'information',
                      'introduction_prisoner',
                      'prisoner',
                      'taxed',
                      'survey',
                      'payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='pd',
        display_name="All in one",
        app_sequence=['introduction',
                      'information',
                      'introduction_prisoner',
                      'prisoner',
                      'survey',
                      'payment_info'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.001, participation_fee=3.00, doc="",
        mturk_hit_settings=dict(
            keywords='bonus, study, experiment, decision',
            title='Decision task against opponent - earn about $3 in 20 minutes',
            description='In this study you will take part in an online multiplayer decision task. $3 for sure, plus bonus ($2 on average). Expected to take 30 minutes',
            frame_height=500,
            template='global/mturk_template.html',
            minutes_allotted_per_assignment=60,
            expiration_hours=7 * 24,
            qualification_requirements=[
                {
                    'QualificationTypeId': "00000000000000000040", # Worker_NumberHITsApproved
                    'Comparator': "GreaterThanOrEqualTo",
                    'IntegerValues': [500]
                },
                {
                    'QualificationTypeId': "000000000000000000L0", # Worker_PercentAssignmentsApproved
                    'Comparator': "GreaterThanOrEqualTo",
                    'IntegerValues': [99]
                },
                {
                    'QualificationTypeId': "00000000000000000071", # Worker_Locale (US only)
                    'Comparator': "EqualTo",
                    'LocaleValues': [{'Country': "US"}]
                },
                # {
                #     'QualificationTypeId': "2F1QJWKUDD8XADTFD2Q0G6UTO95ALH", # Masters
                #     'Comparator': "Exists",
                # },
            ]
            # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
),
)

PARTICIPANT_FIELDS = ['treatment', 'finished_rounds', 'strike', 'is_dropout', 'past_group_id']
SESSION_FIELDS = ['cont_prob_percent', 'min_time',
                  'z', 'r', 't', 'r_percent',
                  'payoff_Idef', 'payoff_both_coop', 'payoff_both_defect', 'payoff_Icoop',
                  'payoff_Idef_t', 'payoff_Icoop_t',
                  'payoff_matrix',
                  'inf_bonus',
                  'coop_label', 'defect_label',
                  'strat_labels',
                  'delta_min', 'delta_risk_dom_min']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '4143000320156'

INSTALLED_APPS = ['otree', 'otreeutils']
