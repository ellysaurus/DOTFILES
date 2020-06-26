
"               d9b                               
"               Y8P                               
 
"      888  888 888 88888b.d88b.  888d888 .d8888b 
"      888  888 888 888  888  88b 888P`  d88P"    
"      Y88  88P 888 888  888  888 888    888      
" d8b   Y8bd8P  888 888  888  888 888    Y88b.    
" Y8P    Y88P   888 888  888  888 888     "Y8888P

"-----------------------------------------------------




" theme settings
set t_Co=256
set termguicolors

"syntax/editor theme
colorscheme miramare "forest-night
let g:miramare_enable_italic = 1
let g:miramare_disable_italic_comment = 1
let g:miramare_transparent_background = 1

set background=dark
let g:airline_powerline_fonts = 1
" other themes: minimalist  term  onedark lucius nord
let g:airline_theme="minimalist"



"------------------- plugins ---------------------
if 0 | endif
if &compatible
  set nocompatible
endif
set runtimepath+=~/.vim/bundle/neobundle.vim/
call neobundle#begin(expand('~/.vim/bundle/'))

NeoBundleFetch 'Shougo/neobundle.vim'
"-------------------------------------
NeoBundle 'ryanoasis/vim-webdevicons'
NeoBundle 'vim-airline/vim-airline-themes'
NeoBundle 'junegunn/goyo.vim'
NeoBundle 'sainnhe/forest-night'
NeoBundle 'neoclide/coc-highlight'
"NeoBundle 'scrooloose/nerdcommenter'
call neobundle#end()
filetype plugin indent on
NeoBundleCheck




"-------------- changing/overwriting vim ariline section ----------------
"this is so no vim theme can change my layout, as some do infact do that.

"setter ecoding og en linux logo     
let g:airline_section_y = '  %{&fileencoding?&fileencoding:&encoding} ' 
"setter en klokke, manjaro logo g så navnet mitt.
let g:airline_section_warning = 'Walter   %{strftime("%H:%M")}'

"------------------------------------------------------------------------





"-----------------------------------------------------------------------
"              SOME OTHER SETTINGS, FOR PLUGINS AND MORE

"using goyo writing mode
	map <F6> :Goyo<CR>
	"map <F5> :Goyo!<CR>
	set linebreak
	set laststatus=2
	set showtabline=2

"binding f3 to tggle line numbers
	noremap <F3> :set invnumber<CR>
	inoremap <F3> <C-O>:set invnumber<CR>
"	set t_Co=256
	set numberwidth=6

"Some basics:
	set number
	set encoding=utf-8
	syntax on
	set title

"split windows side by side:
	set splitbelow splitright

"Shortcutsfor navigating splitted windows:
	map <C-h> <C-w>h
	map <C-j> <C-w>j
	map <C-k> <C-w>k
	map <C-K> <C-w>l
"Shortcuts for resizing vim splits:
    noremap <silent> <C-Left> :vertical resize +1<CR>
    noremap <silent> <C-Right> :vertical resize -1<CR>
    noremap <silent> <C-Up> :resize +1<CR>
    noremap <silent> <C-Down> :resize -1<CR>


"Remapping copy and paste commands:
	vnoremap <C-c> "+y
	map <C-v> "+P

"mapping binds to move display up and down displaylines and not file lines.
	noremap <Up> gk
	noremap! <Up> <C-O>gk
	noremap <Down> gj
	noremap! <Down> <C-O>gj

" the following are optional, to move by file lines using Alt-arrows
	noremap! <M-Up> <Up>
	noremap! <M-Down> <Down>
	noremap <M-Up> k
	noremap <M-Down> j

"Nerd tree
	filetype plugin indent on

"Make nerd tree start with vim
"	autocmd vimenter * NERDTree

"Allow to toggle nert tree on/off
	map <C-n> :NERDTreeToggle<CR>

"Mappe ikoner
	let g:NERDTreeDirArrowExpandable = ' ' " 
	let g:NERDTreeDirArrowCollapsible = ' ' " 

"Show hidden files for nerd tree
	let NERDTreeShowHidden=1

"endre split border
	set fillchars+=vert:\│

"tab settings, slik at det ikke er whitespace, men faktisk mellomrom. setter også til 4 spaces
	set expandtab
	set tabstop=4

"
 
"-----------------------------------------------------------------------------------------------
"fjerner bakrunden fra vim temaet denne er satt på bunnen for å sikre at den kjører etter at tema blir kjørt
	"hi Normal guibg=NONE ctermbg=NONE 
