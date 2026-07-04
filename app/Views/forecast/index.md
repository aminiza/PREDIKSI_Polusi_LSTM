<?= $this->extend('layouts/template') ?>

<?= $this->section('content') ?>

<div class="row">

    <?php if (session()->getFlashdata('success')) : ?>

        <div class="alert alert-success">

            <?= session()->getFlashdata('success') ?>

        </div>

    <?php endif; ?>


    <?php if (session()->getFlashdata('error')) : ?>

        <div class="alert alert-danger">

            <?= session()->getFlashdata('error') ?>

        </div>

    <?php endif; ?>

    <!-- Upload Card -->
    <div class="col-lg-5">

        <div class="card card-primary">

            <div class="card-header">

                <h3 class="card-title">
                    Upload Dataset CSV
                </h3>

            </div>

            <div class="card-body">

                <form action="<?= base_url('forecast/predict') ?>"
                    method="post"
                    enctype="multipart/form-data">

                    <div class="form-group">

                        <label>

                            Pilih File CSV

                        </label>

                        <input
                            type="file"
                            name="dataset"
                            class="form-control"
                            accept=".csv"
                            required>
                    </div>

                    <button
                        class="btn btn-primary btn-block">

                        <i class="fas fa-play-circle"></i>

                        Predict

                    </button>

                </form>

            </div>

        </div>

    </div>

    <!-- Prediction Result -->

    <div class="col-lg-7">

        <div class="card card-success">

            <div class="card-header">

                <h3 class="card-title">

                    Prediction Result

                </h3>

            </div>

            <div class="card-body">

                <div class="row">

                    <div class="col-md-6 mb-3">

                        <div class="small-box bg-info">

                            <div class="inner">

                                <h3>--</h3>

                                <p>Predicted PM2.5</p>

                            </div>

                            <div class="icon">

                                <i class="fas fa-smog"></i>

                            </div>

                        </div>

                    </div>

                    <div class="col-md-6 mb-3">

                        <div class="small-box bg-success">

                            <div class="inner">

                                <h3>READY</h3>

                                <p>Model Status</p>

                            </div>

                            <div class="icon">

                                <i class="fas fa-check-circle"></i>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>

</div>

<!-- Information -->

<div class="row">

    <div class="col-12">

        <div class="card">

            <div class="card-header">

                <h3 class="card-title">

                    Model Information

                </h3>

            </div>

            <div class="card-body">

                <table class="table table-bordered">

                    <tr>

                        <th width="30%">
                            Dataset
                        </th>

                        <td>
                            Air Pollution in China
                        </td>

                    </tr>

                    <tr>

                        <th>
                            Model
                        </th>

                        <td>
                            Stacked LSTM
                        </td>

                    </tr>

                    <tr>

                        <th>
                            Sequence Length
                        </th>

                        <td>
                            24
                        </td>

                    </tr>

                    <tr>

                        <th>
                            Total Features
                        </th>

                        <td>
                            18 Selected Features
                        </td>

                    </tr>

                    <tr>

                        <th>
                            Prediction Target
                        </th>

                        <td>
                            PM2.5 (µg/m³)
                        </td>

                    </tr>

                </table>

            </div>

        </div>

    </div>

</div>

<?= $this->endSection() ?>