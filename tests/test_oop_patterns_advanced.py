import unittest
from oop import oop_patterns_advanced

class TestOOPPatternsAdvanced(unittest.TestCase):
    def test_observer_pattern(self):
        subj = oop_patterns_advanced.Subject()
        result = []
        observer = lambda d: result.append(d)
        subj.attach(observer)
        subj.notify('test')
        self.assertIn('test', result)
        subj.detach(observer)  # Should not raise
        # Detach again should raise ValueError
        with self.assertRaises(ValueError):
            subj.detach(observer)
        # Notify with no observers should not fail
        subj.notify('no observer')

    def test_strategy_pattern(self):
        sorter = oop_patterns_advanced.Sorter(oop_patterns_advanced.QuickSort())
        self.assertEqual(sorter.sort([3, 1, 2]), [1, 2, 3])
        sorter.strategy = oop_patterns_advanced.ReverseSort()
        self.assertEqual(sorter.sort([3, 1, 2]), [3, 2, 1])

    def test_decorator_pattern(self):
        class TestNotifier(oop_patterns_advanced.Notifier):
            def __init__(self):
                self.sent = []
            def send(self, msg):
                self.sent.append(msg)
        base = TestNotifier()
        email = oop_patterns_advanced.EmailDecorator(base)
        sms = oop_patterns_advanced.SMSDecorator(email)
        sms.send('msg')
        self.assertIn('msg', base.sent)

    def test_adapter_pattern(self):
        old = oop_patterns_advanced.OldAPI()
        new = oop_patterns_advanced.NewAPI()
        adapter = oop_patterns_advanced.APIAdapter(new)
        self.assertEqual(old.do_thing(), 'Old API')
        self.assertEqual(adapter.do_thing(), 'New API')

    def test_command_pattern(self):
        class TestCommand(oop_patterns_advanced.Command):
            def __init__(self):
                self.executed = False
            def execute(self):
                self.executed = True
        cmd = TestCommand()
        invoker = oop_patterns_advanced.Invoker()
        invoker.add_command(cmd)
        invoker.run()
        self.assertTrue(cmd.executed)

    def test_dependency_injection(self):
        service = oop_patterns_advanced.Service()
        client = oop_patterns_advanced.Client(service)
        self.assertEqual(client.operate(), 'Service did work')

    def test_fluent_interface(self):
        q = oop_patterns_advanced.QueryBuilder().where('x=1').order_by('y').build()
        self.assertIn('WHERE x=1', q)
        self.assertIn('ORDER BY y', q)

    def test_event_emitter(self):
        emitter = oop_patterns_advanced.EventEmitter()
        result = []
        emitter.on('event', lambda x: result.append(x))
        emitter.emit('event', 123)
        self.assertIn(123, result)

    def test_plugin_architecture(self):
        class TestPlugin(oop_patterns_advanced.PluginBase):
            def __init__(self):
                self.ran = False
            def run(self):
                self.ran = True
        pm = oop_patterns_advanced.PluginManager()
        plugin = TestPlugin()
        pm.register(plugin)
        pm.run_all()
        self.assertTrue(plugin.ran)

if __name__ == "__main__":
    unittest.main()
