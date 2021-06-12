from labml import tracker, experiment
from numpy.random import random


def main():
    conf = {'batch_size': 20}

    with experiment.record(name='sample', exp_conf=conf, writers={'web_api', 'screen'}):
        for i in range(10_000):
            values = {'loss': random()}
            # if i > 1000:
            #     raise RuntimeError('Testing error')
            # for j in range(0, 100):
            #     values[f'grad.fc.{j}.l1'] = random()
            #     values[f'grad.fc.{j}.l2'] = random()
            #     values[f'grad.fc.{j}.mean'] = random()
            #
            #     # values[f'param.fc.{j}.l1'] = random()
            #     # values[f'param.fc.{j}.l2'] = random()
            #     # values[f'param.fc.{j}.mean'] = random()
            #     #
            #     # values[f'module.fc.{j}.l1'] = random()
            #     # values[f'module.fc.{j}.l2'] = random()
            #     # values[f'module.fc.{j}.mean'] = random()
            #     #
            #     # values[f'time.fc.{j}.l1'] = random()
            #     # values[f'time.fc.{j}.l2'] = random()
            #     # values[f'time.fc.{j}.mean'] = random()
            tracker.save(i, values)

            if i % 1000 == 0:
                tracker.new_line()


def repeat_values():
    conf = {'batch_size': 20}

    with experiment.record(name='sample', exp_conf=conf, writers={'web_api', 'screen'}):
        for i in range(10):
            tracker.add_global_step(1)
            tracker.save('loss', 1)
            tracker.save('loss', 5)
            # tracker.save()

            if i % 1000 == 0:
                tracker.new_line()


if __name__ == '__main__':
    # main()
    repeat_values()
