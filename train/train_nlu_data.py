from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from nlu_intent_recog.models import Intent
import os
import time


def train_data():
    generate_train_data()
    base_dir = os.path.abspath(os.path.dirname(__file__))
    training_data = load_data(base_dir + '/nlu_data/nlu.md')
    trainer = Trainer(config.load(base_dir + "/config/nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(base_dir + '/models/', fixed_model_name="nlu_intent_module")  # Returns the directory the model is stored in


def generate_train_data():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    t = time.time()
    training_data_tmp_file = base_dir + '/nlu_data/nlu'+str(round(t * 1000))+'.md'
    file = open(training_data_tmp_file, 'w+')
    for i in Intent.objects.all():
        lines=['## intent:' + i.intent + '\n']
        for q in i.questions.all():
            lines.append('- ' + q.question_text + '\n')
        file.writelines(lines)
    file.close()
    training_data_file = base_dir + '/nlu_data/nlu.md'
    os.rename(training_data_tmp_file,training_data_file)