test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all([type(q21_proportion_books_200_224) != type(...), type(q21_proportion_books_200_224) != None])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= q21_proportion_books_200_224 <= 1
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
