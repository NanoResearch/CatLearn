import time

localtime = time.asctime(time.localtime(time.time()))
dt = ' Run on %s\n' % localtime


def write_data_setup(function, data):
    """ Write output for the datasetup functions. """
    with open('ATOMLout.txt', 'a+') as writefile:
        if function is 'get_unique':
            writefile.write('Output from atoml.get_unique.' + dt)
            writefile.write('index, target\n(training size is ' +
                            str(len(data['taken'])) + ')\n')
            for i, j in zip(data['taken'], data['target']):
                writefile.write(str(i) + ', ' + str(j) + '\n')
            writefile.write('\nEnd of get_unique function.\n \n')

        if function is 'get_train':
            writefile.write('Output from atoml.get_train.' + dt)
            writefile.write('index, target\n(training size is ' +
                            str(len(data['order'])) + ')\n')
            for i, j in zip(data['order'], data['target']):
                writefile.write(str(i) + ', ' + str(j) + '\n')
            writefile.write('\nEnd of get_train function.\n \n')

        if function is 'data_split':
            writefile.write('Output from atoml.data_split.' + dt)
            s = 'index set_1, target set_1, '
            for i in list(range(len(data['split_cand']) - 1)):
                s += 'index set_' + str(i + 2) + ', target set_' + str(i + 2)
            writefile.write(s + '\n(training size is ' +
                            str([len(data['split_cand'][i]) for i in
                                 list(range(len(data['split_cand'])))]) +
                            ')\n')
            for r in list(range(len(data['split_cand'][0]))):
                row = str(data['index'][0][r]) + ', ' + str(
                    data['target'][0][r])
                for l in list(range(len(data['split_cand']) - 1)):
                    while (len(data['index'][l + 1]) <
                           len(data['split_cand'][0])):
                        data['index'][l + 1].append(None)
                        data['target'][l + 1].append(None)
                    row += ', ' + str(data['index'][l + 1][r]) + ', ' + str(
                        data['target'][l + 1][r])
                writefile.write(str(row) + '\n')
            writefile.write('\nEnd of get_train function.\n \n')

        if function is 'remove_outliers':
            writefile.write('Output from atoml.remove_outliers.' + dt)
            writefile.write('Index of candidates removed:\n' +
                            str(data['removed']) + '\n')
            writefile.write('\nEnd of remove_outliers function.\n \n')

        if function is 'target_standardize':
            writefile.write('Output from atoml.target_standardize.' + dt)
            writefile.write('Target mean is: ' + str(data['mean']) + '\n')
            writefile.write('Target standard deviation is: ' +
                            str(data['std']) + '\n')
            writefile.write('\nEnd of target_standardize function.\n \n')


def write_fingerprint_setup(function, data):
    """ Write output for the fingerprint functions. """
    with open('ATOMLout.txt', 'a+') as writefile:
        if function is 'return_fpv':
            writefile.write('Output from atoml.return_fpv.' + dt)
            writefile.write('Use prior: ' + str(data['prior'][0]) +
                            '\nGenerator names:\n' + str(data['names']) + '\n')
            writefile.write('\nEnd of return_fpv function.\n \n')

        if function is 'standardize':
            writefile.write('Output from atoml.standardize.' + dt)
            writefile.write('Feature mean is:\n' + str(data['mean']) +
                            '\nFeature standard deviation is:\n' +
                            str(data['std']) + '\n')
            writefile.write('\nEnd of standardize function.\n \n')

        if function is 'normalize':
            writefile.write('Output from atoml.normalize.' + dt)
            writefile.write('Feature mean is:\n' + str(data['mean']) +
                            '\nFeature difference is:\n' +
                            str(data['dif']) + '\n')
            writefile.write('\nEnd of normalize function.\n \n')

        if function is 'sure_independence_screening':
            st = 'Output from atoml.sure_independence_screening.' + dt
            writefile.write(st)
            writefile.write('Correlation is:\n' + str(data['ordered_corr']))
            if 'accepted' in data:
                writefile.write('\nAccepted features are:\n' +
                                str(data['accepted']))
            if 'rejected' in data:
                writefile.write('\nRejected features are:\n' +
                                str(data['rejected']) + '\n')
            writefile.write('\nEnd of sure_independence_screening function.\n \
                            \n')

        if function is 'iterative_sis':
            writefile.write('Output from atoml.iterative_sis.' + dt)
            writefile.write('Correlation is:\n' + str(data['correlation']))
            if 'accepted' in data:
                writefile.write('\nAccepted features are:\n' +
                                str(data['accepted']))
            if 'rejected' in data:
                writefile.write('\nRejected features are:\n' +
                                str(data['rejected']) + '\n')
            writefile.write('\nEnd of iterative_sis function.\n \n')


def write_predict(function, data):
    """ Write output for the fingerprint functions. """
    with open('ATOMLout.txt', 'a+') as writefile:
        if function is 'get_predictions':
            writefile.write('Output from atoml.get_predictions.' + dt)
            writefile.write('Training error is: ' +
                            str(data['training_rmse']['average']) + '\n')
            if 'uncertainty' in data:
                writefile.write('prediction, error, uncertainty\n')
                for i, j, k in zip(data['prediction'],
                                   data['validation_rmse']['all'],
                                   data['uncertainty']):
                    writefile.write(str(i) + ', ' + str(j) + ', ' + str(k) +
                                    '\n')
            else:
                writefile.write('prediction, error\n')
                for i, j in zip(data['prediction'],
                                data['validation_rmse']['all']):
                    writefile.write(str(i) + ', ' + str(j) + '\n')
            writefile.write('\nEnd of get_predictions function.\n \n')
