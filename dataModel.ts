// Solo
interface Solo {
  title: string;
  composer: string;
  category: 'marimba' | 'xylophone' | 'vibraphone' | 'snare' | 'timpani' | 'multi percussion';
  subCategory: 'two_mallets' | 'four_mallets' | 'marching' | 'concert' | null;
  difficulty: 1 | 2 | 3 | 4 | 5 | null; // easy easy-medium medium medium-advanced advanced
  duration: string | null; // example 2:00
  description: string | null;
  isBook: boolean;
  publisher: 'tapspace';
  videoURL: string | null;
  audioURL: string | null;
}
