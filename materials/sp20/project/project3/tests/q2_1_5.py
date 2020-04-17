test = {
  'name': 'q2_1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [most_common('Genre', close_movies.take(range(k))) for k in range(1, 5, 1)]
          ['thriller', 'thriller', 'thriller', 'thriller']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> [most_common('Genre', close_movies.take(np.arange(4, k, -1))) for k in range(3, -1, -1)]
          ['comedy', 'comedy', 'comedy', 'thriller']
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
