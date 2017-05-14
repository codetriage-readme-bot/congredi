import unittest
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
warning = bcolors.WARNING + 'Timing Warning' + bcolors.ENDC + \
    ': Test Took ' + bcolors.BOLD + '%.2f' + bcolors.ENDC + \
    's (threshold ' + bcolors.FAIL + '%.2f' + bcolors.ENDC + 's)'


class TimedTestCase(unittest.TestCase):

    threshold = 0

    def setUp(self):
        #print('ran setup for %s' % self.id())
        self.threshold = .5
        self._time_started = time.time()

    def tearDown(self):
        elapsed = time.time() - self._time_started
        if elapsed > self.threshold:
            print((warning % (elapsed, self.threshold)))

source = b"""
Hello, *world*! This is a ~~good~~marvelous day!
Here is an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk

You can also have fenced code blocks:

```
import this
```
"""

source2 = b"""
Hello, *world*! This is a ~~good~~marvelous day!
Here was an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk
- [x] ten


```
import this
```
"""
empty = b""
empty2 = b"""


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu viverra lacus. Vestibulum a est a felis posuere pellentesque ac sit amet sem. Aliquam erat volutpat. Phasellus eleifend, felis eget lobortis dapibus, ligula purus rhoncus massa, placerat pharetra urna lacus vel ex. Proin finibus pellentesque dui id mollis. Vestibulum id nibh libero. Quisque at odio velit. Morbi ac viverra velit, ut elementum erat. Cras varius, odio sit amet rutrum porta, purus mi sollicitudin sem, vel rutrum nisl augue non arcu. Fusce sagittis sem commodo lorem malesuada, eu vestibulum lacus laoreet. Proin nibh dolor, blandit sed dictum in, imperdiet nec risus. Quisque sem est, ultrices consequat urna id, malesuada vestibulum lacus. Nullam congue lectus sed mollis sagittis. Vestibulum pellentesque vulputate lacus sed consectetur.

Etiam gravida justo vel venenatis convallis. Vestibulum a nunc at justo vestibulum mattis quis eget erat. Sed semper hendrerit orci. In in sapien vitae purus sodales gravida vel et nunc. Fusce porttitor, ante molestie blandit laoreet, massa libero commodo ex, at suscipit lacus dolor a elit. Aenean ut erat non sapien blandit ullamcorper eget sit amet velit. Nullam mattis nulla a urna maximus pellentesque vel in enim. Nullam lorem dui, ullamcorper id velit et, consequat porta justo. Duis lacus ipsum, finibus eget est ut, accumsan interdum augue. Maecenas convallis sed enim non rhoncus. Vestibulum at commodo nisl, id ultricies ex. Morbi nunc est, semper et efficitur ac, porta ut leo. Donec eu facilisis justo.

Maecenas congue suscipit lacus vitae rhoncus. Donec dictum lacinia elementum. Proin fringilla ante elit. Maecenas lacus arcu, eleifend non consectetur non, aliquet tincidunt lectus. Duis a fringilla massa, sed varius neque. Phasellus placerat non risus a finibus. Curabitur ut eros mattis, ornare purus ac, volutpat ante. Mauris at auctor ligula, et lacinia metus. Ut vitae neque mattis, placerat sem et, blandit neque. Donec rutrum, neque non feugiat laoreet, enim nibh pharetra purus, eu tincidunt nisi metus id lacus. Vestibulum efficitur venenatis velit, quis sodales orci laoreet et. Nunc vestibulum non tortor eget tempor. Duis congue nunc eu gravida consectetur. Vivamus sagittis ante nec erat accumsan, nec interdum risus varius. Nullam ac turpis blandit, viverra augue ultrices, pellentesque mauris. Nulla eu faucibus ante.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus molestie nibh vel felis consequat, ut consectetur arcu porta. Duis in tortor ultrices mi malesuada mattis at quis turpis. Morbi enim nunc, accumsan id leo eget, egestas blandit dolor. Aenean id sapien quis quam sollicitudin laoreet in in lacus. Suspendisse potenti. Donec ut erat malesuada, tempus nunc ac, sodales ante. Phasellus ac felis ultricies, ullamcorper ipsum sed, vehicula urna. Nullam ac lacus euismod, fermentum justo a, ornare massa. Vestibulum sed mollis nulla. Nulla turpis tellus, porttitor a sodales ac, lacinia sodales ex. Donec scelerisque magna vel nisi cursus malesuada. Aenean vehicula dictum enim, eu semper nisi dictum nec. Nunc in leo varius, sagittis odio in, rhoncus purus.

Nulla facilisi. Vestibulum aliquet est a ex lobortis vulputate. Curabitur at ultrices orci. Vestibulum varius nulla eu aliquet finibus. Donec id posuere est. Donec sit amet lacus vitae nulla dapibus imperdiet sed id ante. Nullam vitae lorem tristique, lobortis justo sit amet, porta erat. Donec quam lorem, ullamcorper sit amet tortor hendrerit, tempor dapibus magna. Cras viverra consectetur odio, quis iaculis lacus ornare vel. Pellentesque id lorem eu sapien vehicula molestie in vitae purus. Sed ac sapien non purus dapibus lacinia. Integer vel nunc vel tortor tempor accumsan. Integer tempor sit amet dolor in posuere. Etiam maximus odio quis felis blandit scelerisque. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
"""
