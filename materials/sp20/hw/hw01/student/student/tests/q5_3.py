test = {
  'name': 'Question 5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(gws_relative_change, (int, float))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(linguistics_relative_change, (int, float))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(rhetoric_relative_change, (int, float))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> gws_relative_change >= 64 and gws_relative_change <= 66
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> linguistics_relative_change >= 36 and linguistics_relative_change <= 38
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> rhetoric_relative_change >= 50 and rhetoric_relative_change <= 52
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
