<?php namespace App\Http\Controllers\Admin;

use App\Http\Requests;
use App\Http\Controllers\Controller;

use Illuminate\Http\Request;
use App\Article as Record;
use View;
use Input;
use Redirect;

class ArticleController extends Controller {

    protected $link = 'admin/article';
    protected $name = 'article';
    protected $path = 'admin.article.';

    public function __construct()
    {
        View::share('link', $this->link);
    }

	/**
	 * Display a listing of the resource.
	 *
	 * @return Response
	 */
	public function index()
	{
        $records = Record::paginate(5);
        return view($this->path . 'index', ['records'=>$records ]);
	}

	/**
	 * Show the form for creating a new resource.
	 *
	 * @return Response
	 */
	public function create()
	{
        return view($this->path . 'create');
	}

	/**
	 * Store a newly created resource in storage.
	 *
	 * @return Response
	 */
	public function store(Request $request)
	{
        /*
        $this->validate($request, [
            'title' => 'required|unique:pages|max:255',
            'body' => 'required',
        ]);
        */

        $record = new Record;
        $record->title = Input::get('title');
        $record->body = Input::get('body');

        if ($record->save()) {
            return Redirect::to($this->link);
        } else {
            return Redirect::back()->withInput()->withErrors('保存失败！');
        }
	}

	/**
	 * Display the specified resource.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function show($id)
	{
		//
	}

	/**
	 * Show the form for editing the specified resource.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function edit($id)
	{
        return view($this->path . 'edit', ['record' => Record::find($id)] );
	}

	/**
	 * Update the specified resource in storage.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function update(Request $request, $id)
	{
        /*
        $this->validate($request, [
            'title' => 'required|unique:pages,title,'.$id.'|max:255',
            'body' => 'required',
        ]);
        */

        $record = Record::find($id);
        $record->title = Input::get('title');
        $record->body  = Input::get('body');

        if ($record->save()) {
            return Redirect::to($this->link);
        } else {
            return Redirect::back()->withInput()->withErrors('保存失败！');
        }
	}

	/**
	 * Remove the specified resource from storage.
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function destroy($id)
	{
        $record = Record::find($id);
        $record->delete();

        return Redirect::to($this->link);
	}

}
