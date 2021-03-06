import ConfigParser
import os
import hashlib


class Config_manager:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.out_folder = None
        
    def set_current_folder(self,t):
        self.cwd = t
        
    def set_config(self,file_cfg):
        self.config.read(file_cfg)
        output_folder_cfg = self.config.get('general','output_folder')
        out_folder = ''
        if os.path.isabs(output_folder_cfg):
            self.out_folder = output_folder_cfg
        else:
            self.out_folder = os.path.join(self.cwd,output_folder_cfg)
            
            
    def get_index_folder(self):
        my_name = 'index_folder'
        index_folder = None
        if self.config.has_option('general', my_name):
            ind_fol = self.config.get('general', my_name)
            if os.path.isabs(ind_fol):
                index_folder = ind_fol
            else:
                index_folder = os.path.join(self.cwd,ind_fol)
        return index_folder
        
    def get_folder_cached_results(self):
        my_name = 'cached_results'
        return os.path.join(self.get_out_folder(),my_name)
    
    def get_name_stored_file(self,pattern, min_freq, limit,fixed=None):
        my_str = "%s_%d_%d" % (pattern, min_freq,limit)
        if fixed is not None:
            my_str+='_'+fixed
            
        key = hashlib.sha256(my_str).hexdigest()
        
        complete_name = os.path.join(self.get_folder_cached_results(),key)
        
        return complete_name
    
    def get_measure_type(self):
        return str(self.config.get('general','measure'))
    
    def get_min_num_seeds_to_appear_with(self):
        return int(self.config.get('general','accept_patterns_with_at_least_num_seeds'))
    
    def get_filename_overall_frequency(self):
        my_name = 'overall_freq_for_pattern.bin'
        return os.path.join(self.get_out_folder(),my_name)
    
    def get_out_folder(self):
        return self.out_folder
    
    def get_seeds(self):
        seeds = self.config.get('general','seeds')
        seeds = [s for s in seeds.strip().split(';') if len(s)!=0]
        return seeds
    
    
    def get_filename_results_pattern(self):
        my_name = 'extracted_patterns.'+self.get_measure_type()+'.xml'
        return os.path.join(self.out_folder,my_name)
    
   
    def get_ngram_len(self):
        return int(self.config.get('general','ngram_len'))
    
    def get_limit_query_pattern(self):
        if self.config.has_option('google_web_query','limit_per_query_pattern_extraction'):
            return int(self.config.get('google_web_query','limit_per_query_pattern_extraction'))
        else:
            return 1000
    
    def get_min_freq_pattern(self):
        if self.config.has_option('google_web_query','min_freq_for_hit_pattern_extraction'):
            return int(self.config.get('google_web_query','min_freq_for_hit_pattern_extraction'))
        else:
            return 100

    def get_limit_query_candidate(self):
        if self.config.has_option('google_web_query','limit_per_query_candidate_selection'):
            return int(self.config.get('google_web_query','limit_per_query_candidate_selection'))
        else:
            return 1000
    
    def get_min_freq_candidate(self):
        if self.config.has_option('google_web_query','min_freq_for_hit_candidate_selection'):
            return int(self.config.get('google_web_query','min_freq_for_hit_candidate_selection'))
        else:
            return 100
        
    def get_percent_selected_patterns(self):
        if self.config.has_option('general', 'percent_selected_patterns'):
            return int(self.config.get('general', 'percent_selected_patterns'))
        else:
            return 25
        
    def get_filename_csv(self):
        my_name = 'candidate_words.'+self.get_measure_type()+'.csv'
        return os.path.join(self.get_out_folder(),my_name)
    
    def get_list_stop_words(self):
        stopwords = []
        if self.config.has_option('general','stop_words_for_patterns'):
            stopwords = self.config.get('general','stop_words_for_patterns')
            stopwords = [s for s in stopwords.strip().split(';') if len(s)!=0]
        return stopwords
    
    def get_templates(self):
        templates = []
        if self.config.has_section('templates'):
            for name, value in self.config.items('templates'):
                #t1=* * X
                templates.append(value)
        return templates
    
    def get_min_patterns_per_candidate(self):
        if self.config.has_option('general', 'min_patterns_per_candidate'):
            return int(self.config.get('general', 'min_patterns_per_candidate'))
        else:
            return 0
                
    def get_filename_candidate_list(self):
        my_name = 'candidate_words.'+self.get_measure_type()+'.xml'
        return os.path.join(self.get_out_folder(),my_name)            
    
            
    