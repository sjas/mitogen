"""
Measure latency of .local() setup.
"""

import mitogen
import time


@mitogen.main()
def main(router):
    t0 = time.time()
    for x in xrange(20):
        t = time.time()
        ctx = router.local()
        ctx.shutdown(wait=True)
        print x, 1000 * (time.time() - t)
    print '++', 1000 * ((time.time() - t0) / (1.0+x))
