@extends('app')

@section('content')
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="panel panel-default">
                    <div class="panel-heading">后台首页</div>
                    <div class="panel-body">

                        <a href="{{ URL("$link/create") }}" class="btn btn-lg btn-primary">新增</a>

                        @foreach ($records as $record)
                            <hr>
                            <div class="page">
                                <h4>{{ $record->title }}</h4>
                                <div class="content">
                                    <p>
                                        {{ $record->body }}
                                    </p>
                                </div>
                            </div>
                            <a href="{{ URL("$link/$record->id/edit") }}" class="btn btn-success">编辑</a>

                            <form action="{{ URL("$link/$record->id") }}" method="POST" style="display: inline;">
                                <input name="_method" type="hidden" value="DELETE">
                                <input type="hidden" name="_token" value="{{ csrf_token() }}">
                                <button type="submit" class="btn btn-danger">删除</button>
                            </form>
                        @endforeach

                    </div>
                    <?php echo $records->render(); ?>
                </div>

            </div>
        </div>

    </div>

@endsection