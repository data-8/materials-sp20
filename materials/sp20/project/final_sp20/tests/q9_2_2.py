test = {
  'name': 'q9_2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(prob_auditors_avg_below_499) != type(...), type(prob_auditors_avg_below_499) != None])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If you are failing this test, you should make sure your answer is a probability between 0 and 1.;
          >>> 0 <= prob_auditors_avg_below_499 <= 1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
